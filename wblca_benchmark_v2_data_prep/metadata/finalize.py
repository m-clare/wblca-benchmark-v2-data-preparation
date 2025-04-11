"""Utility functions for src.data.finalize."""

# from pathlib import Path
from typing import List
from logging import getLogger
from functools import reduce
import pandas as pd
# pylint: disable=W0703, W0719

finalize_logger = getLogger("metadata.finalize")


def calculate_new_columns(df: pd.DataFrame, col_finalize: dict) -> pd.DataFrame:
    """
    Calculate new columns for analysis.

    This function creates new columns according to the following criteria:
        - Calculate "GFA Without Parking (ft2)" as: GFA with Parking - GFA Parking
        - Calculate "GFA With Parking (m2)" as: GFA With Parking (ft2) * (ft2 to m2 conversion)
        - Calculate "GFA Without Parking (m2)" as:/
    GFA Without Parking (ft2) * (ft2 to m2 conversion)
        - Calculate "GFA Primary Use (m2)" as: GFA Primary Use (ft2) * (ft2 to m2 conversion)
        - Calculate "GFA Secondary Use (m2)" as: GFA Secondary Use (ft2) * (ft2 to m2 conversion)
    Creates regions based on NRMCA regions
        - Calculate "GFA Parking (m2)" as: GFA Parking (ft2) * (ft2 to m2 conversion)
        - Calculate "GFA Added (m2)" as: GFA Added (ft2) * (ft2 to m2 conversion)
        - Calculate "GFA Renovated (m2)" as: GFA Renovated (ft2) * (ft2 to m2 conversion)
        - Calculate "Building Height (m)" as: Building Height * (ft to m conversion)
        - Calculate "Thermal Envelope Area (m2)" as: Thermal Envelope Area * (ft2 to m2 conversion)
        - Calculate "Typical Column Grid, Long Direction (m)" as: \
            Typical Column Grid, Long Direction * (ft to m conversion)
        - Calculate "Typical Column Grid, Short Direction (m)" as: \
            Typical Column Grid, Short Direction * (ft to m conversion)
        - Calculate "Ultimate Wind Speed (mps)" as: Ultimate Wind Speed * (mph to mps conversion)
        - Calculate "LCA Assessment Year" as: Date of Analysis converted to year
        - Calculate "Country" using create_country function
        - Calculate "Region" using create_region function
        - Calculate "Building Code Year" using create_bldg_code_year function
        - Calculate "Building Energy Code Year" using create_bldg_energy_code_year function
        - Calculate "Interiors" as a column if both interiors are included in assessment.

    Args:
        df (pd.DataFrame): DataFrame to add new columns
        col_finalize (dict): Dictionary with configuration necessary for column creation

    Returns:
        pd.DataFrame: DataFrame with new columns added
    """
    # factors to be used by column calulations
    ft_to_m_factor = 0.3048
    ft2_to_m2_factor = 0.092903
    mph_to_m_per_s_factor = 0.44704

    # create calculated columns
    try:
        finalize_logger.info("Creating calculated columns.")
        df["GFA Without Parking (ft2)"] = df["GFA With Parking (ft2)"].fillna(0) - df[
            "GFA Parking (ft2)"
        ].fillna(0)
        df["GFA With Parking (m2)"] = (
            df["GFA With Parking (ft2)"].fillna(0) * ft2_to_m2_factor
        )
        df["GFA Without Parking (m2)"] = (
            df["GFA Without Parking (ft2)"].fillna(0) * ft2_to_m2_factor
        )
        df["GFA Primary Use (m2)"] = (
            df["GFA Primary Use (ft2)"].fillna(0) * ft2_to_m2_factor
        )
        df["GFA Secondary Use (m2)"] = df["GFA Secondary Use (ft2)"] * ft2_to_m2_factor
        df["GFA Parking (m2)"] = df["GFA Parking (ft2)"] * ft2_to_m2_factor
        df["GFA Added (m2)"] = df["GFA Added (ft2)"] * ft2_to_m2_factor
        df["GFA Renovated (m2)"] = df["GFA Renovated (ft2)"] * ft2_to_m2_factor
        df["Building Height (m)"] = df["Building Height"] * ft_to_m_factor
        df["Thermal Envelope Area (m2)"] = (
            df["Thermal Envelope Area"] * ft2_to_m2_factor
        )
        df["Typical Column Grid, Long Direction (m)"] = (
            df["Typical Column Grid, Long Direction"] * ft_to_m_factor
        )
        df["Typical Column Grid, Short Direction (m)"] = (
            df["Typical Column Grid, Short Direction"] * ft_to_m_factor
        )
        df["Ultimate Wind Speed (mps)"] = (
            df["Ultimate Wind Speed"] * mph_to_m_per_s_factor
        )

        # create lca_assessment_year
        df["LCA Assessment Year"] = pd.to_datetime(df["Date of Analysis"]).dt.strftime(
            "%Y"
        )

        # create calculated columns from config file
        df["Country"] = create_country(df, col_finalize)
        df["Region"] = create_regions(df, col_finalize)
    except IndexError as ie:
        finalize_logger.exception(
            "Could not find column in DataFrame for calculated columns"
        )
        raise IndexError("Could not find column in DataFrame") from ie
    finalize_logger.info("Created calculated columns.")

    # interiors designation
    df["Interiors"] = "No"
    df.loc[
        (df["Interiors - Construction"] == "Yes")
        | (df["Interiors - Finishes"] == "Yes"),
        "Interiors",
    ] = "Yes"
    finalize_logger.debug("Creating column for interior designation.")

    finalize_logger.info("Finished creating calculated columns.")

    return df


def calculate_bins(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate new bins for analysis.

    This function creates custom binned columns for the following columns:
        - Stories Above Grade
        - Stories Below Grade
        - GFA With Parking (ft2)
        - Building Height
        - Building Height (m)
        - Occupant Load
        - Residential Units
        - Software Version

    This function also creates bins for:
        - physical scope using physical_scope_bins function
        - structural material using structural_material_bins function

    Args:
        df (pd.DataFrame): DataFrame to add new bins

    Returns:
        pd.DataFrame: DataFrame with new columns added
        str: logged info of written csv
    """
    finalize_logger.info("Begin calculating bins.")
    finalize_logger.info("Calculating Stories Above Grade bins.")
    df["Stories Above Grade_bins"] = pd.cut(
        df["Stories Above Grade"],
        bins=[0, 1, 5, 10, 15, 20, 100],
        include_lowest=True,
        labels=["1", "2 to 5", "6 to 10", "11 to 15", "16 to 20", "21 or more"],
    )
    finalize_logger.info("Calculated Stories Above Grade bins.")

    finalize_logger.info("Calculating Stories Below Grade bins.")
    df["Stories Below Grade_bins"] = pd.cut(
        df["Stories Below Grade"],
        bins=[-1, 0, 1, 2, 3, 100],
        include_lowest=False,
        labels=["0", "1", "2", "3", "4 or more"],
    )
    finalize_logger.info("Calculated Stories Below Grade bins.")

    finalize_logger.info("Calculating GFA With Parking (ft2) bins.")
    df["GFA With Parking(ft2)_bins"] = pd.cut(
        df["GFA With Parking (ft2)"],
        bins=[0, 10000, 50000, 100000, 200000, 400000, 1000000000],
        include_lowest=True,
        labels=[
            "10,000 ft2 or less",
            "10,001-50,000 ft2",
            "50,001-100,000 ft2",
            "100,001-200,000 ft2",
            "200,001-400,000 ft2",
            "Over 400,000 ft2",
        ],
    )
    finalize_logger.info("Calculated GFA With Parking (ft2) bins.")

    finalize_logger.info("Calculating GFA With Parking (m2) bins.")
    df["GFA With Parking(m2)_bins"] = pd.cut(
        df["GFA With Parking (ft2)"],
        bins=[0, 1000, 5000, 10000, 15000, 35000, 1000000000],
        include_lowest=True,
        labels=[
            "1,000 m2 or less",
            "1,001-5,000 m2",
            "5,001-10,000 m2",
            "10,001-15,000 m2",
            "15,001-35,000 m2",
            "Over 35,000 m2",
        ],
    )
    finalize_logger.info("Calculated GFA With Parking (m2) bins.")

    finalize_logger.info("Calculating Building Height bins.")
    df["Building Height_bins"] = pd.cut(
        df["Building Height"],
        bins=[0, 25, 50, 75, 100, 150, 200, 300, 1000000000],
        include_lowest=True,
        labels=[
            "0-25 ft",
            "26-50 ft",
            "51-75 ft",
            "76-100 ft",
            "101-150 ft",
            "151-200 ft",
            "201-300 ft",
            "Over 300 ft",
        ],
    )
    finalize_logger.info("Calculated Building Height bins.")

    finalize_logger.info("Calculating Building Height (m) bins.")
    df["Building Height_m_bins"] = pd.cut(
        df["Building Height (m)"],
        bins=[0, 7.5, 15, 22.5, 30, 45, 60, 90, 1000000000],
        include_lowest=True,
        labels=[
            "0-7.5 m",
            "7.6-15 m",
            "15.1-22.5 m",
            "22.6-30 m",
            "31-45 m",
            "46-60 m",
            "61-90 m",
            "Over 90 m",
        ],
    )
    finalize_logger.info("Calculated Building Height (m) bins.")

    finalize_logger.info("Calculating Software version bins.")
    df["Software Version_bins"] = "Other"
    df.loc[df["Software Version"].str.contains("Oneclick"), "Software Version_bins"] = (
        "One Click LCA"
    )
    df.loc[df["Software Version"].str.contains("Tally"), "Software Version_bins"] = (
        "Tally LCA"
    )
    finalize_logger.info("Calculated Software version bins.")

    df["physical_scope_bins"] = physical_scope_bins(df)
    df["structural_material_bins"] = structural_material_bins(df)

    finalize_logger.info("End calculating bins.")

    return df


def and_loc(
    df: pd.DataFrame,
    result: str | bool,
    col_to_modify: str,
    and_filters: List[pd.Series],
) -> pd.Series:
    """
    Wrap pandas loc function to include multiple criteria combined with & operator.

    Args:
        df (pd.DataFrame): DataFrame of One Click entries
        result (str): Value to be applied to pysical_scope_bins column
        and_filters (List[pd.Series]): Filters applied for loc function

    Raises:
        ValueError: Review one of the and_filter values
    """
    for fil in and_filters:
        if fil is None:
            finalize_logger.exception(
                "One of the and_filters was not entered correctly"
            )
            raise KeyError("One of the and_filters was not entered correctly")

    and_filters_reduced = reduce(
        lambda series_one, series_two: series_one & series_two, and_filters
    )

    df.loc[and_filters_reduced, col_to_modify] = result
    return df[col_to_modify]


def physical_scope_bins(df: pd.DataFrame) -> pd.Series:
    """
    Create the physical scope_bins column with custom filtering.

    Args:
        df (pd.DataFrame): DataFrame to be updated

    Returns:
        pd.Series: "physical_scope_bins" column
    """
    finalize_logger.info("Begin calculating physical scope bins.")
    # set column value
    df["physical_scope_bins"] = ""

    # set filters
    substr = df["Substructure"] == "Yes"
    superstr = df["Shell - Superstructure"] == "Yes"
    enc = df["Shell - Enclosure"] == "Yes"
    int_con = df["Interiors - Construction"] == "Yes"
    int_fin = df["Interiors - Finishes"] == "Yes"

    # appends a letter based on if the scope is included
    df.loc[(substr), "physical_scope_bins"] += "B"
    df.loc[(superstr), "physical_scope_bins"] += "S"
    df.loc[enc, "physical_scope_bins"] += "E"
    df.loc[(int_con), "physical_scope_bins"] += "C"
    df.loc[(int_fin), "physical_scope_bins"] += "F"
    finalize_logger.info("End calculating physical scope bins.")

    return df["physical_scope_bins"]


def structural_material_bins(df: pd.DataFrame) -> pd.Series:
    """
    Create the structural_material_bins column with custom filtering.

    Args:
        df (pd.DataFrame): DataFrame to be updated

    Returns:
        pd.Series: "structural_material_bins" column
    """
    finalize_logger.info("Begin calculating structural material bins.")
    df["structural_material_bins"] = None

    # set filters
    horiz_steel = df["Primary Horizontal Gravity System"].str.contains("Steel")
    horiz_concrete = df["Primary Horizontal Gravity System"].str.contains("Concrete")
    horiz_wood = df["Primary Horizontal Gravity System"].str.contains("Wood")
    vert_steel = df["Primary Vertical Gravity System"].str.contains("Steel")
    vert_concrete = df["Primary Vertical Gravity System"].str.contains("Concrete")
    vert_wood = df["Primary Vertical Gravity System"].str.contains("Wood")
    vert_mass_timber = df["Primary Vertical Gravity System"].str.contains(
        "Wood: Mass timber"
    )
    vert_light_frame = df["Primary Vertical Gravity System"].str.contains(
        "Wood: Light-frame"
    )
    vert_masonry = df["Primary Vertical Gravity System"].str.contains("Masonry")
    # lat_steel = df['Primary Lateral Force Resisting System'].str.contains('Steel')
    lat_wood = df["Primary Lateral Force Resisting System"].str.contains("Wood")
    lat_concrete = df["Primary Lateral Force Resisting System"].str.contains("Concrete")
    lat_masonry = df["Primary Lateral Force Resisting System"].str.contains("Masonry")

    # Steel filters
    finalize_logger.info("Begin applying steel filters.")
    df["structural_material_bins"] = and_loc(
        df=df,
        result="Steel",
        col_to_modify="structural_material_bins",
        and_filters=[
            horiz_steel,
            vert_steel,
        ],
    )
    finalize_logger.info("End applying steel filters.")

    # Concrete filters
    finalize_logger.info("Begin applying concrete filters.")
    df["structural_material_bins"] = and_loc(
        df=df,
        result="Concrete",
        col_to_modify="structural_material_bins",
        and_filters=[
            horiz_concrete,
            vert_concrete,
        ],
    )
    finalize_logger.info("End applying concrete filters.")

    # Steel/Concrete filters
    finalize_logger.info("Begin applying steel/concrete filters.")
    df["structural_material_bins"] = and_loc(
        df=df,
        result="Steel/Concrete",
        col_to_modify="structural_material_bins",
        and_filters=[
            horiz_steel,
            vert_concrete,
        ],
    )
    df["structural_material_bins"] = and_loc(
        df=df,
        result="Steel/Concrete",
        col_to_modify="structural_material_bins",
        and_filters=[
            horiz_concrete,
            vert_steel,
        ],
    )
    df["structural_material_bins"] = and_loc(
        df=df,
        result="Steel/Concrete",
        col_to_modify="structural_material_bins",
        and_filters=[horiz_steel, vert_steel, lat_concrete],
    )
    finalize_logger.info("End applying steel/concrete filters.")

    # Steel/Masonry filters
    finalize_logger.info("Begin applying steel/masonry filters.")
    df["structural_material_bins"] = and_loc(
        df=df,
        result="Steel/Masonry",
        col_to_modify="structural_material_bins",
        and_filters=[
            horiz_steel,
            vert_masonry,
        ],
    )
    df["structural_material_bins"] = and_loc(
        df=df,
        result="Steel/Masonry",
        col_to_modify="structural_material_bins",
        and_filters=[horiz_steel, vert_steel, lat_masonry],
    )
    finalize_logger.info("End applying steel/masonry filters.")

    # Other filters
    finalize_logger.info("Begin applying other filters.")
    df["structural_material_bins"] = and_loc(
        df=df,
        result="Other",
        col_to_modify="structural_material_bins",
        and_filters=[vert_wood, horiz_concrete],
    )
    df["structural_material_bins"] = and_loc(
        df=df,
        result="Other",
        col_to_modify="structural_material_bins",
        and_filters=[vert_wood, horiz_steel],
    )
    df["structural_material_bins"] = and_loc(
        df=df,
        result="Other",
        col_to_modify="structural_material_bins",
        and_filters=[horiz_wood, vert_concrete],
    )
    df["structural_material_bins"] = and_loc(
        df=df,
        result="Other",
        col_to_modify="structural_material_bins",
        and_filters=[horiz_wood, vert_steel],
    )
    df["structural_material_bins"] = and_loc(
        df=df,
        result="Other",
        col_to_modify="structural_material_bins",
        and_filters=[horiz_wood, vert_masonry],
    )
    df["structural_material_bins"] = and_loc(
        df=df,
        result="Other",
        col_to_modify="structural_material_bins",
        and_filters=[horiz_wood, vert_wood, lat_concrete],
    )
    df["structural_material_bins"] = and_loc(
        df=df,
        result="Other",
        col_to_modify="structural_material_bins",
        and_filters=[horiz_concrete, vert_steel, lat_wood],
    )
    finalize_logger.info("End applying other filters.")

    # Wood: Mass Timber filters
    finalize_logger.info("Begin applying wood: mass timber filters.")
    df["structural_material_bins"] = and_loc(
        df=df,
        result="Wood: Mass Timber",
        col_to_modify="structural_material_bins",
        and_filters=[vert_mass_timber, horiz_wood],
    )
    finalize_logger.info("End applying wood: mass timber filters.")

    # Wood: Light-frame filters
    finalize_logger.info("Begin applying wood: light frame filters.")
    df["structural_material_bins"] = and_loc(
        df=df,
        result="Wood: Light-frame",
        col_to_modify="structural_material_bins",
        and_filters=[vert_light_frame, horiz_wood],
    )
    finalize_logger.info("End applying wood: light frame filters.")

    finalize_logger.info("End calculating structural material bins.")

    return df["structural_material_bins"]


def create_country(df: pd.DataFrame, col_finalize: dict) -> pd.Series:
    """Create Countries based on state information from metadata.

    Args:
        df (pd.DataFrame): dataframe to be updated
        col_finalize (dict): dictionary with countries and their corresponding states

    Returns:
        pd.Series: dataframe with country column
    """
    finalize_logger.info("Begin creating country designation.")
    united_states = col_finalize.get("united_states")
    assert united_states is not None, "The united states list could not be set"

    canada = col_finalize.get("canada")
    assert canada is not None, "The canada list could not be set"

    mexico = col_finalize.get("mexico")
    assert mexico is not None, "The mexico list could not be set"

    # set other values
    df["Country"] = "Other"

    # set regions
    df.loc[df["Project State or Province"].isin(united_states), "Country"] = (
        "United States"
    )
    df.loc[df["Project State or Province"].isin(canada), "Country"] = "Canada"
    df.loc[df["Project State or Province"].isin(mexico), "Country"] = "Mexico"
    finalize_logger.info("End creating country designation.")

    return df["Country"]


def create_regions(df: pd.DataFrame, col_finalize: dict) -> pd.Series:
    """Create regions based on state information from metadata.

    Args:
        df (pd.DataFrame): dataframe to be updated
        col_finalize (dict): dictionary with regions and their corresponding states

    Returns:
        pd.Series: dataframe with region column
    """
    finalize_logger.info("Begin creating region designation.")
    nrmca_eastern = col_finalize.get("nrmca_eastern")
    assert nrmca_eastern is not None, "The nrmca eastern list could not be set"

    nrmca_great_lakes_midwest = col_finalize.get("nrmca_great_lakes_midwest")
    assert nrmca_great_lakes_midwest is not None, (
        "The nrmca great lakes list could not be set"
    )

    nrmca_north_central = col_finalize.get("nrmca_north_central")
    assert nrmca_north_central is not None, (
        "The nrmca north central list could not be set"
    )

    nrmca_pacific_northwest = col_finalize.get("nrmca_pacific_northwest")
    assert nrmca_pacific_northwest is not None, (
        "The nrmca pacific nw list could not be set"
    )

    nrmca_pacific_southwest = col_finalize.get("nrmca_pacific_southwest")
    assert nrmca_pacific_southwest is not None, (
        "The nrmca pacific sw list could not be set"
    )

    nrmca_rocky_mountains = col_finalize.get("nrmca_rocky_mountains")
    assert nrmca_rocky_mountains is not None, (
        "The nrmca rocky mountain list could not be set"
    )

    nrmca_south_central = col_finalize.get("nrmca_south_central")
    assert nrmca_south_central is not None, (
        "The nrmca south central list could not be set"
    )

    nrmca_south_eastern = col_finalize.get("nrmca_south_eastern")
    assert nrmca_south_eastern is not None, (
        "The nrmca south eastern list could not be set"
    )

    # set canadian values
    df["Region"] = "Canada"
    # set regions
    df.loc[df["Project State or Province"].isin(nrmca_eastern), "Region"] = "Eastern"
    df.loc[
        df["Project State or Province"].isin(nrmca_great_lakes_midwest), "Region"
    ] = "Great Lakes Midwest"
    df.loc[df["Project State or Province"].isin(nrmca_north_central), "Region"] = (
        "North Central"
    )
    df.loc[df["Project State or Province"].isin(nrmca_pacific_northwest), "Region"] = (
        "Pacific Northwest"
    )
    df.loc[df["Project State or Province"].isin(nrmca_pacific_southwest), "Region"] = (
        "Pacific Southwest"
    )
    df.loc[df["Project State or Province"].isin(nrmca_rocky_mountains), "Region"] = (
        "Rocky Mountains"
    )
    df.loc[df["Project State or Province"].isin(nrmca_south_central), "Region"] = (
        "South Central"
    )
    df.loc[df["Project State or Province"].isin(nrmca_south_eastern), "Region"] = (
        "South Eastern"
    )
    finalize_logger.info("End creating region designation.")

    return df["Region"]

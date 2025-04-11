"""Utility functions for use in the harmonization workflow for src.clean.clean."""

from pathlib import Path
from logging import getLogger
import pandas as pd
from wblca_benchmark_v2_data_prep.lca_results.enums import RevitBuildingCategory
# pylint: disable=E1130, W0718, C0103, W0719

clean_logger = getLogger("lca_results.clean")


def clean_tally_df(tally_df: pd.DataFrame, tally_file: Path) -> pd.DataFrame:
    """Clean all the column information from the raw WBLCA output for Tally models.

    Args:
        tally_df (pd.DataFrame): raw dataframe of Tally Models
        tally_file (Path): File path location for tally model

    Returns:
        pd.DataFrame: Cleaned Tally dataframes
    """
    clean_logger.info("Begin cleaning tally dataframe.")
    tally_df["CLF Model ID"] = tally_file.stem
    tally_df["Tool"] = "TallyLCA"
    tally_df = tally_df.set_index("CLF Model ID")

    clean_logger.info("Create CLF Omni column")
    if "CLF Omni" in tally_df.columns:
        tally_df["CLF Omni"] = tally_df["CLF Omni"].replace(
            {
                "Shell - Substructure": "Substructure",
                "Shell - Enclosure": "Shell - Exterior Enclosure",
            }
        )
    else:
        tally_df["CLF Omni"] = None

    clean_logger.info("Ensure revit building element exists.")
    if "Revit building element" not in tally_df.columns:
        tally_df["Revit building element"] = "Not included"
    tally_df["Revit building element"] = tally_df["Revit building element"].astype(
        object
    )

    if "file_name_before_merge" not in tally_df.columns:
        tally_df["file_name_before_merge"] = "Not a merged file"

    clean_logger.info("Ensure MQ_1 and MQ_2 exist.")
    tally_df["MQ_1"] = "Other"
    tally_df["MQ_2"] = "Other"
    clean_logger.info("End cleaning tally dataframe.")

    return tally_df


def clean_oneclick_df(oneclick_df: pd.DataFrame, oneclick_file: Path) -> pd.DataFrame:
    """Clean all the column information from the raw WBLCA output for One Click LCA models.

    Args:
        oneclick_df (pd.DataFrame): raw dataframe of One Click LCA Models
        oneclick_file (Path): File path location for One Click LCA Models

    Returns:
        pd.DataFrame: Cleaned One Click LCA dataframes
    """
    clean_logger.info("Begin cleaning oneclick dataframe.")
    mass_and_env_impacts = [
        "Acidification kg SO₂e",
        "Eutrophication kg Ne",
        "Ozone Depletion kg CFC11e",
        "Formation of tropospheric ozone kg O3e",
        "Depletion of nonrenewable energy MJ",
        "Global warming kg CO₂e",
        "Biogenic carbon storage kg CO₂e bio",
        "Mass of raw materials kg",
    ]

    oneclick_df["CLF Model ID"] = oneclick_file.stem
    oneclick_df["Tool"] = "One Click LCA"
    oneclick_df = oneclick_df.set_index("CLF Model ID")
    clean_logger.info("Clean rows that are not itemized material impacts.")
    oneclick_df = oneclick_df[~pd.isna(oneclick_df["Section"])]
    oneclick_df[mass_and_env_impacts] = oneclick_df[mass_and_env_impacts].replace(
        "-", 0
    )

    clean_logger.info("Create CLF Omni column")
    if "CLF Omni" in oneclick_df.columns:
        oneclick_df["CLF Omni"] = oneclick_df["CLF Omni"].replace(
            {
                "Shell - Substructure": "Substructure",
                "Shell - Enclosure": "Shell - Exterior Enclosure",
            }
        )
    else:
        oneclick_df["CLF Omni"] = None

    clean_logger.info("Ensure Omniclass exists.")
    if "Omniclass" not in oneclick_df.columns:
        oneclick_df["Omniclass"] = "Not included"

    clean_logger.info("Ensure csiMasterformat exists.")
    if "csiMasterformat" not in oneclick_df.columns:
        oneclick_df["csiMasterformat"] = 0

    clean_logger.info("Ensure Question exists.")
    if "Question" not in oneclick_df.columns:
        oneclick_df["Question"] = "Not included"

    if "file_name_before_merge" not in oneclick_df.columns:
        oneclick_df["file_name_before_merge"] = "Not a merged file"

    if "Design Name" not in oneclick_df.columns:
        oneclick_df["Design Name"] = "No design options"

    clean_logger.info("Ensure MQ_1 and MQ_2 exist.")
    oneclick_df["MQ_1"] = "Other"
    oneclick_df["MQ_2"] = "Other"

    oneclick_df = adjust_oneclick_csi_division(oneclick_df)
    clean_logger.info("End cleaning oneclick dataframe.")

    return oneclick_df


def adjust_tally_walls(df: pd.DataFrame) -> pd.DataFrame:
    """Adjusts revit building element values for wall objects in tally entries.

    Args:
        df (pd.DataFrame): DataFrame of Tally entries

    Raises:
        KeyError: raised if loc function does not work due to invalid key

    Returns:
        pd.DataFrame: DataFrame with updated revit building element values
    """
    clean_logger.info("Begin adjusting tally wall revit building element values.")
    rt_c_wall = df["Revit category"].str.fullmatch("Walls")

    rt_fn_int = df["Revit family name"].str.contains(
        "int|Int|INT|interior|Interior|INTERIOR"
    )
    rt_fn_ext = df["Revit family name"].str.contains(
        "ext|Ext|EXT|exterior|Exterior|EXTERIOR"
    )
    rt_fn_rainscreen = df["Revit family name"].str.contains(
        "rainscreen|Rainscreen|RAINSCREEN"
    )
    rt_fn_parapet = df["Revit family name"].str.contains("parapet|Parapet|PARAPET")
    rt_fn_soffit = df["Revit family name"].str.contains("soffit|Soffit|SOFFIT")
    rt_fn_partition = df["Revit family name"].str.contains(
        "partition|Partition|PARTITION"
    )
    rt_fn_enc = df["Revit family name"].str.contains(
        "enc|Enc|ENC|enclosure|Enclosure|ENCLOSURE"
    )

    try:
        df.loc[(rt_c_wall) & (rt_fn_ext), "Revit building element"] = (
            RevitBuildingCategory.ENCLOSURE.value
        )
        df.loc[(rt_c_wall) & (rt_fn_rainscreen), "Revit building element"] = (
            RevitBuildingCategory.ENCLOSURE.value
        )
        df.loc[(rt_c_wall) & (rt_fn_parapet), "Revit building element"] = (
            RevitBuildingCategory.ENCLOSURE.value
        )
        df.loc[(rt_c_wall) & (rt_fn_soffit), "Revit building element"] = (
            RevitBuildingCategory.ENCLOSURE.value
        )
        df.loc[(rt_c_wall) & (rt_fn_enc), "Revit building element"] = (
            RevitBuildingCategory.ENCLOSURE.value
        )
        df.loc[(rt_c_wall) & (rt_fn_int), "Revit building element"] = (
            RevitBuildingCategory.INTERIORS.value
        )
        df.loc[(rt_c_wall) & (rt_fn_partition), "Revit building element"] = (
            RevitBuildingCategory.INTERIORS.value
        )
    except KeyError as key:
        clean_logger.exception(
            "In the process of adjusting wall objects, a key error occured"
        )
        raise KeyError(
            "In the process of adjusting wall objects, a key error occured"
        ) from key
    except Exception as e:
        clean_logger.exception("an error has occured")
        print(f"an error has occured: {e}")

    clean_logger.info("End adjusting tally wall revit building element values.")
    return df


def adjust_oneclick_csi_division(df: pd.DataFrame) -> pd.DataFrame:
    """Adjusts one click csi divisions for better element mapping.

    Args:
        df (pd.DataFrame): DataFrame of One Click LCA entries

    Raises:
        KeyError: raised if loc function does not work due to invalid key

    Returns:
        pd.DataFrame: DataFrame with updated csi division values
    """
    clean_logger.info("Begin adjusting oneclick csi division values.")
    # csiMasterformat filters
    oc_csi_eight = df["csiMasterformat"] == 8
    oc_csi_ten = df["csiMasterformat"] == 10
    oc_csi_thirty_one = df["csiMasterformat"] == 31

    nat_stone_cat_mat_two = df["Resource type"].str.contains(
        "natural stone|Natural stone|Natural Stone"
    )
    bcr_cat_mat_three = df["Name"].str.contains("BCR")
    door_cat_mat_three = df["Name"].str.contains("door|Door|DOOR")
    lock_cat_mat_three = df["Name"].str.contains("lock|Lock|LOCK")
    sanitary_cat_mat_three = df["Name"].str.contains("sanitary|Sanitary|SANITARY")
    window_frame_cat_mat_three = df["Name"].str.contains(
        "window frame|Window frame|Window Frame"
    )
    aggregate_cat_mat_three = df["Name"].str.contains("aggregate|Aggregate|AGGREGATE")
    sand_cat_mat_three = df["Name"].str.contains("sand|Sand|SAND")
    tel_dock_lev_cat_mat_three = df["Name"].str.contains(
        "telescopic dock leveler|Telescopic dock leveler|Telescopic Dock Leveler"
    )

    try:
        df.loc[(oc_csi_thirty_one) & (nat_stone_cat_mat_two), "csiMasterformat"] = 4
        df.loc[(oc_csi_ten) & (bcr_cat_mat_three), "csiMasterformat"] = 3
        df.loc[(oc_csi_ten) & (door_cat_mat_three), "csiMasterformat"] = 8
        df.loc[(oc_csi_ten) & (lock_cat_mat_three), "csiMasterformat"] = 8
        df.loc[(oc_csi_ten) & (sanitary_cat_mat_three), "csiMasterformat"] = 22
        df.loc[(oc_csi_ten) & (window_frame_cat_mat_three), "csiMasterformat"] = 8
        df.loc[(oc_csi_thirty_one) & (aggregate_cat_mat_three), "csiMasterformat"] = 3
        df.loc[(oc_csi_thirty_one) & (sand_cat_mat_three), "csiMasterformat"] = 3
        df.loc[(oc_csi_eight) & (tel_dock_lev_cat_mat_three), "csiMasterformat"] = 12

    except KeyError as key:
        clean_logger.exception(
            "In the process of adjusting csi division, a key error occured"
        )
        raise KeyError(
            "In the process of adjusting csi division, a key error occured"
        ) from key
    except Exception as e:
        clean_logger.exception("an error has occured")
        print(f"an error has occured: {e}")
    clean_logger.info("End adjusting oneclick csi division values.")

    return df


def read_excel(file_path: Path) -> pd.DataFrame:
    """Read csv files for general use.

    Args:
        file_path (Path): file path of csv to read

    Raises:
        PermissionError: Raised if function does not have permission to access file
        IOError: Raised if file cannot be read
        Exception: General exception just in case

    Returns:
        pd.DataFrame: DataFrame of read csv file
    """
    try:
        clean_logger.info("Reading %s", file_path.stem)
        df = pd.read_excel(
            file_path,
        )
    except PermissionError as pe:
        clean_logger.exception("Permission Error probably caused by having file open")
        raise PermissionError("Try closing out the file you are trying to read") from pe
    except IOError as io:
        clean_logger.exception("IO Error for excel file")
        raise IOError("Trouble reading excel file") from io
    except Exception as e:
        clean_logger.exception("Unknown error has occurred.")
        raise Exception("An unknown error has occured") from e
    clean_logger.info("Read data from file %s", file_path.name)

    return df

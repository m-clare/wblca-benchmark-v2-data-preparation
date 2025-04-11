#!/usr/bin/env python
from pathlib import Path
import os
import pandas as pd
import wblca_benchmark_v2_data_prep.lca_results.clean as clean_util
import wblca_benchmark_v2_data_prep.utils.general as general_util
from wblca_benchmark_v2_data_prep.lca_results.MappingImplementation import (
    TallyElementMapper,
    TallyMaterialQuantityMapper,
)
import wblca_benchmark_v2_data_prep.lca_results.tally_ele_filters as t_efi
import wblca_benchmark_v2_data_prep.lca_results.tally_mat_filters as t_mfi


def clean_raw_tally_files(tally_dir):
    """Clean raw tally files for further analysis.

    - Reads tally files from input directory
    - Cleans tally files
    - adjusts the csi division of tally walls
    - returns cleaned tally dataframes
    """
    cleaned_dfs = []
    for tally_file in tally_dir.glob("*.csv"):
        # read tally files
        tally_df = general_util.read_csv(tally_file)
        tally_df = clean_util.clean_tally_df(tally_df=tally_df, tally_file=tally_file)
        adjusted_tally_df = clean_util.adjust_tally_walls(tally_df)
        cleaned_dfs.append(adjusted_tally_df)

    return cleaned_dfs


def clean_raw_oneclick_files(oneclick_dir):
    """Clean raw One Click LCA files for further analysis.

    This script does the following:

    - Reads oneclick files in raw directory
    - Cleans oneclick files
    - writes oneclick files to cleaned directory
    """
    cleaned_dfs = []
    for oneclick_file in oneclick_dir.glob("*.xlsx"):
        # read oneclick files
        oneclick_df = clean_util.read_excel(oneclick_file)
        oneclick_df = clean_util.clean_oneclick_df(
            oneclick_df=oneclick_df, oneclick_file=oneclick_file
        )
        cleaned_dfs.append(oneclick_df)

    return cleaned_dfs


def add_stored_carbon_to_tally_dfs(tally_dfs):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    reference_dir = os.path.join(base_dir, "../../references/stored_carbon_database.xlsx")
    stored_bio_database_path = Path(reference_dir)
    full_stored_bio_database = pd.read_excel(stored_bio_database_path, sheet_name="csc")
    stored_bio_data_short = full_stored_bio_database[
        ["Name_Tally Material", "Stored Carbon (C02eq/kg)"]
    ]
    merged_dfs = []
    for tally_df in tally_dfs:
        merged_tally_df = tally_df.merge(
            right=stored_bio_data_short,
            left_on="Material Name",
            right_on="Name_Tally Material",
            how="left",
        )
        merged_tally_df["Stored Biogenic Carbon"] = 0.0
        merged_tally_df.loc[
            (merged_tally_df["Life Cycle Stage"] == "[A1-A3] Product")
            | (merged_tally_df["Life Cycle Stage"] == "Product"),
            "Stored Biogenic Carbon",
        ] = (
            merged_tally_df["Mass Total (kg)"] * merged_tally_df["Stored Carbon (C02eq/kg)"]
        )
        merged_dfs.append(merged_tally_df)
    return merged_dfs


def map_tally_elements(tally_dfs):
    """Maps Tally elements.

    This function does the following:

    - Instantiates filters created in tally_ele_filters
    - Instantiates a mapper object
    - Loops through the filters and applies them to the tally dataframe
    - Returns the element mapped df
    """
    tally_filters = [
        t_efi.CurtainWallPanels("CLF Omni"),
        t_efi.CurtainWallMullions("CLF Omni"),
        t_efi.Doors("CLF Omni"),
        t_efi.Floors("CLF Omni"),
        t_efi.Roofs("CLF Omni"),
        t_efi.Railings("CLF Omni"),
        t_efi.Stairs("CLF Omni"),
        t_efi.StructuralColumns("CLF Omni"),
        t_efi.StructuralConnections("CLF Omni"),
        t_efi.StructuralFoundations("CLF Omni"),
        t_efi.StructuralFraming("CLF Omni"),
        t_efi.Walls("CLF Omni"),
        t_efi.Windows("CLF Omni"),
    ]

    element_mapped_dfs = []
    for tally_df in tally_dfs:
        Mapper = TallyElementMapper(tally_df, t_efi.Ceilings("CLF Omni"))
        Mapper.do_filtering()

        for fil in tally_filters:
            Mapper.change_filter_type(fil)
            Mapper.do_filtering()
        element_mapped_dfs.append(Mapper.df)
    return element_mapped_dfs


def map_tally_materials(tally_dfs):
    tally_material_quantity_one_filters = [
        t_mfi.ConcreteMaterialQuantityOne("MQ_1"),
        t_mfi.SteelMaterialQuantityOne("MQ_1"),
        t_mfi.MasonryMaterialQuantityOne("MQ_1"),
        t_mfi.AluminumMaterialQuantityOne("MQ_1"),
        t_mfi.WoodMaterialQuantityOne("MQ_1"),
        t_mfi.GlazingMaterialQuantityOne("MQ_1"),
        t_mfi.RoofMaterialQuantityOne("MQ_1"),
        t_mfi.InsulationMaterialQuantityOne("MQ_1"),
        t_mfi.GypsumMaterialQuantityOne("MQ_1"),
        t_mfi.FireproofMaterialQuantityOne("MQ_1"),
    ]
    tally_material_quantity_two_filters = [
        t_mfi.ConcreteMaterialQuantityTwo("MQ_2"),
        t_mfi.SteelMaterialQuantityTwo("MQ_2"),
        t_mfi.MasonryMaterialQuantityTwo("MQ_2"),
        t_mfi.AluminumMaterialQuantityTwo("MQ_2"),
        t_mfi.WoodMaterialQuantityTwo("MQ_2"),
        t_mfi.GlazingMaterialQuantityTwo("MQ_2"),
        t_mfi.RoofMaterialQuantityTwo("MQ_2"),
        t_mfi.InsulationMaterialQuantityTwo("MQ_2"),
        t_mfi.GypsumMaterialQuantityTwo("MQ_2"),
        t_mfi.FireproofMaterialQuantityTwo("MQ_2"),
    ]
    tally_material_quantity_one_other_filters = [
        t_mfi.DoorFrameMaterialQuantityOneOther("MQ_1"),
        t_mfi.WindowFrameMaterialQuantityOneOther("MQ_1"),
        t_mfi.AcousticCeilingsMaterialQuantityOneOther("MQ_1"),
        t_mfi.SyntheticCompositesMaterialQuantityOneOther("MQ_1"),
        t_mfi.CladdingMaterialQuantityOneOther("MQ_1"),
        t_mfi.AdhesivesMaterialQuantityOneOther("MQ_1"),
        t_mfi.AirVaporMaterialQuantityOneOther("MQ_1"),
        t_mfi.CoatingsMaterialQuantityOneOther("MQ_1"),
        t_mfi.FloorTileMaterialQuantityOneOther("MQ_1"),
        t_mfi.WallCoveringsMaterialQuantityOneOther("MQ_1"),
        t_mfi.OtherMetalsMaterialQuantityOneOther("MQ_1"),
    ]
    tally_material_quantity_two_other_filters = [
        t_mfi.DoorFrameMaterialQuantityTwoOther("MQ_2"),
        t_mfi.WindowFrameMaterialQuantityTwoOther("MQ_2"),
        t_mfi.AcousticCeilingsMaterialQuantityTwoOther("MQ_2"),
        t_mfi.SyntheticCompositesMaterialQuantityTwoOther("MQ_2"),
        t_mfi.CladdingMaterialQuantityTwoOther("MQ_2"),
        t_mfi.AdhesivesMaterialQuantityTwoOther("MQ_2"),
        t_mfi.AirVaporMaterialQuantityTwoOther("MQ_2"),
        t_mfi.CoatingsMaterialQuantityTwoOther("MQ_2"),
        t_mfi.FloorTileMaterialQuantityTwoOther("MQ_2"),
        t_mfi.OtherMetalsMaterialQuantityTwoOther("MQ_2"),
    ]
    tally_material_quantity_two_unique_other_filters = [
        t_mfi.FinalOtherMaterialQuantityTwoOther("MQ_2")
    ]

    mq_tally_dfs = []
    for tally_df in tally_dfs:
        MaterialQuantityOneMapper = TallyMaterialQuantityMapper(
            tally_df,
        )

        for fil in tally_material_quantity_one_filters:
            MaterialQuantityOneMapper.change_filter_type(fil)
            MaterialQuantityOneMapper.do_filtering()

        material_quantity_one_updated_tally_df = MaterialQuantityOneMapper.df

        # instantiate Material Mapper for Material Quantity Two using updated df
        MaterialQuantityTwoMapper = TallyMaterialQuantityMapper(
            material_quantity_one_updated_tally_df,
        )

        for fil in tally_material_quantity_two_filters:
            MaterialQuantityTwoMapper.change_filter_type(fil)
            MaterialQuantityTwoMapper.do_filtering()

        mq_one_and_two_updated_tally_df = MaterialQuantityTwoMapper.df

        # instantiate Material Mapper for Material Quantity one of other materials using updated df
        MaterialQuantityOneOtherMapper = TallyMaterialQuantityMapper(
            mq_one_and_two_updated_tally_df,
        )

        for fil in tally_material_quantity_one_other_filters:
            MaterialQuantityOneOtherMapper.change_filter_type(fil)
            MaterialQuantityOneOtherMapper.do_filtering()

        mq_one_two_and_other_one_updated_tally_df = MaterialQuantityOneOtherMapper.df

        # instantiate Material Mapper for Material Quantity Two using updated df
        MaterialQuantityTwoOtherMapper = TallyMaterialQuantityMapper(
            mq_one_two_and_other_one_updated_tally_df,
        )

        for fil in tally_material_quantity_two_other_filters:
            MaterialQuantityTwoOtherMapper.change_filter_type(fil)
            MaterialQuantityTwoOtherMapper.do_filtering()

        mq_one_two_and_other_one_two_updated_tally_df = MaterialQuantityTwoOtherMapper.df

        # instantiate Material Mapper for Material Quantity Two using updated df
        MaterialQuantityTwoFinalOtherMapper = TallyMaterialQuantityMapper(
            mq_one_two_and_other_one_two_updated_tally_df,
        )

        for fil in tally_material_quantity_two_unique_other_filters:
            MaterialQuantityTwoFinalOtherMapper.change_filter_type(fil)
            MaterialQuantityTwoFinalOtherMapper.do_filtering()

        mq_tally_dfs.append(MaterialQuantityTwoFinalOtherMapper.df)
    return mq_tally_dfs


def run_tally(tally_dir=None):
    path = Path(tally_dir)
    cleaned_tally_dfs = clean_raw_tally_files(path)
    sc_tally_dfs = add_stored_carbon_to_tally_dfs(cleaned_tally_dfs)
    element_mapped_dfs = map_tally_elements(sc_tally_dfs)
    material_mapped_dfs = map_tally_materials(element_mapped_dfs)

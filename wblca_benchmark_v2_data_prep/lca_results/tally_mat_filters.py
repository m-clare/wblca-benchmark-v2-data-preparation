# pylint: disable=C0103, W0718
"""Defines Tally Filter classes to update values in Material Quantity Columns"""

from typing import Dict
import pandas as pd
from wblca_benchmark_v2_data_prep.lca_results.abstract_filters import AbstractFilter
from wblca_benchmark_v2_data_prep.lca_results.enums import (
    MaterialQuantityOne,
    MaterialQuantityTwo,
)


class ConcreteMaterialQuantityOne(AbstractFilter):
    """Method to update MQ_1 column for Concrete entries."""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=MaterialQuantityOne.CONCRETE.value,
            and_filters=[
                all_filters.get("conc_cat_mat_one"),
                all_filters.get("conc_cat_mat_two"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityOne.CONCRETE.value,
            and_filters=[all_filters.get("conc_cat_mat_two")],
            or_filters=[
                all_filters.get("self_lvl_under_cat_mat_three"),
                all_filters.get("gfrc_cat_mat_three"),
                all_filters.get("str_conc_cat_mat_three"),
                all_filters.get("lw_conc_cat_mat_three"),
            ],
        )
        return df


class SteelMaterialQuantityOne(AbstractFilter):
    """Method to update MQ_1 column for Steel entries."""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=MaterialQuantityOne.STEEL.value,
            and_filters=[
                all_filters.get("steel_cat_ele_four"),
                all_filters.get("metal_cat_mat_two"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityOne.STEEL.value,
            and_filters=[
                all_filters.get("stair_cat_ele_four"),
                all_filters.get("metals_cat_mat_one"),
                all_filters.get("metal_cat_mat_two"),
            ],
        )
        self.or_loc(
            df=df,
            result=MaterialQuantityOne.STEEL.value,
            or_filters=[
                all_filters.get("gal_steel_support_cat_mat_three"),
                all_filters.get("chromium_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityOne.OTHER.value,
            and_filters=[
                all_filters.get("stair_cat_ele_four"),
                all_filters.get("metals_cat_mat_one"),
                all_filters.get("metal_cat_mat_two"),
                all_filters.get("aluminum_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityOne.STEEL.value,
            and_filters=[
                all_filters.get("metal_cat_mat_two"),
                all_filters.get("reinf_rod_cat_mat_three"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityOne.STEEL.value,
            and_filters=[
                all_filters.get("metal_cat_mat_two"),
            ],
            or_filters=[
                all_filters.get("reinf_cmc_cat_mat_three"),
                all_filters.get("alt_reinf_cmc_cat_mat_three"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityOne.STEEL.value,
            and_filters=[
                all_filters.get("metal_cat_mat_two"),
            ],
            or_filters=[
                all_filters.get("reinf_csri_cat_mat_three"),
                all_filters.get("alt_reinf_csri_cat_mat_three"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityOne.STEEL.value,
            and_filters=[
                all_filters.get("metal_cat_mat_two"),
            ],
            or_filters=[
                all_filters.get("reinf_weld_w_cat_mat_three"),
                all_filters.get("reinf_woven_w_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityOne.STEEL.value,
            and_filters=[
                all_filters.get("steel_cable_cat_mat_three"),
                all_filters.get("pr_conc_bm_cat_mat_four"),
            ],
        )
        return df


class MasonryMaterialQuantityOne(AbstractFilter):
    """Method to update MQ_1 column for Masonry entries."""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        df.loc[all_filters.get("stone_cat_mat_two"), self.column_name_to_change] = (
            MaterialQuantityOne.MASONRY.value
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityOne.MASONRY.value,
            and_filters=[
                all_filters.get("masonry_cat_mat_one"),
            ],
            or_filters=[
                all_filters.get("conc_cat_mat_two"),
                all_filters.get("masonry_cat_mat_two"),
            ],
        )
        self.or_loc(
            df=df,
            result=MaterialQuantityOne.MASONRY.value,
            or_filters=[
                all_filters.get("mortar_cat_mat_three"),
                all_filters.get("grout_cat_mat_three"),
            ],
        )
        return df


class AluminumMaterialQuantityOne(AbstractFilter):
    """Method to update MQ_1 column for Aluminum entries."""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        df.loc[
            all_filters.get("aluminum_cat_mat_three"), self.column_name_to_change
        ] = MaterialQuantityOne.ALUMINUM.value
        self.and_or_loc(
            df=df,
            result=MaterialQuantityOne.OTHER.value,
            and_filters=[
                all_filters.get("aluminum_cat_mat_three"),
            ],
            or_filters=[
                all_filters.get("alum_faced_comp_cat_mat_three"),
                all_filters.get("siding_cat_mat_three"),
                all_filters.get("door_cat_mat_three"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityOne.OTHER.value,
            and_filters=[
                all_filters.get("aluminum_cat_mat_three"),
            ],
            or_filters=[
                all_filters.get("ins_metal_cat_mat_four"),
                all_filters.get("metal_wall_cat_mat_four"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityOne.OTHER.value,
            and_filters=[
                all_filters.get("aluminum_cat_mat_four"),
            ],
            or_filters=[
                all_filters.get("ceil_sys_cat_ele_four"),
                all_filters.get("door_cat_ele_four"),
                all_filters.get("window_frame_cat_ele_four"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityOne.ALUMINUM.value,
            and_filters=[
                all_filters.get("aluminum_cat_mat_three"),
                all_filters.get("extru_cat_mat_three"),
            ],
        )
        df.loc[
            all_filters.get("alum_mull_sys_cat_mat_five"), self.column_name_to_change
        ] = MaterialQuantityOne.OTHER.value
        return df


class WoodMaterialQuantityOne(AbstractFilter):
    """Method to update MQ_1 column for Wood entries."""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        df.loc[all_filters.get("wood_cat_mat_two"), self.column_name_to_change] = (
            MaterialQuantityOne.WOOD.value
        )
        return df


class GlazingMaterialQuantityOne(AbstractFilter):
    """Method to update MQ_1 column for Glazing entries."""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        df.loc[all_filters.get("glazing_cat_mat_two"), self.column_name_to_change] = (
            MaterialQuantityOne.GLAZING.value
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityOne.OTHER.value,
            and_filters=[
                all_filters.get("glazing_cat_mat_two"),
                all_filters.get("door_cat_ele_four"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityOne.GLAZING.value,
            and_filters=[
                all_filters.get("spandrel_cat_mat_two"),
                all_filters.get("glass_cat_mat_three"),
            ],
        )
        return df


class RoofMaterialQuantityOne(AbstractFilter):
    """Method to update MQ_1 column for Roofing entries."""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        df.loc[all_filters.get("roof_mem_cat_mat_two"), self.column_name_to_change] = (
            MaterialQuantityOne.ROOF.value
        )
        self.or_loc(
            df=df,
            result=MaterialQuantityOne.ROOF.value,
            or_filters=[
                all_filters.get("roof_cat_mat_three"),
                all_filters.get("roof_start_cat_mat_three"),
                all_filters.get("roof_cat_mat_four"),
                all_filters.get("roof_start_cat_mat_four"),
                all_filters.get("roofing_cat_mat_three"),
                all_filters.get("roofing_start_cat_mat_three"),
                all_filters.get("sbs_cat_mat_three"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityOne.OTHER.value,
            and_filters=[
                all_filters.get("roof_cat_mat_three"),
            ],
            or_filters=[
                all_filters.get("fireproof_cat_mat_two"),
                all_filters.get("insulation_cat_mat_two"),
                all_filters.get("floor_tile_cat_mat_two"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityOne.OTHER.value,
            and_filters=[
                all_filters.get("roof_start_cat_mat_three"),
            ],
            or_filters=[
                all_filters.get("fireproof_cat_mat_two"),
                all_filters.get("insulation_cat_mat_two"),
                all_filters.get("floor_tile_cat_mat_two"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityOne.OTHER.value,
            and_filters=[
                all_filters.get("roofing_cat_mat_three"),
            ],
            or_filters=[
                all_filters.get("fireproof_cat_mat_two"),
                all_filters.get("insulation_cat_mat_two"),
                all_filters.get("floor_tile_cat_mat_two"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityOne.OTHER.value,
            and_filters=[
                all_filters.get("roofing_start_cat_mat_three"),
            ],
            or_filters=[
                all_filters.get("fireproof_cat_mat_two"),
                all_filters.get("insulation_cat_mat_two"),
                all_filters.get("floor_tile_cat_mat_two"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityOne.OTHER.value,
            and_filters=[
                all_filters.get("sbs_cat_mat_three"),
            ],
            or_filters=[
                all_filters.get("fireproof_cat_mat_two"),
                all_filters.get("insulation_cat_mat_two"),
                all_filters.get("floor_tile_cat_mat_two"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityOne.OTHER.value,
            and_filters=[
                all_filters.get("insul_cat_mat_four"),
            ],
            or_filters=[
                all_filters.get("roof_cat_mat_four"),
                all_filters.get("roof_start_cat_mat_four"),
            ],
        )
        return df


class InsulationMaterialQuantityOne(AbstractFilter):
    """Method to update MQ_1 column for Insulation entries."""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        df.loc[
            all_filters.get("insulation_cat_mat_two"), self.column_name_to_change
        ] = MaterialQuantityOne.INSULATION.value
        self.and_or_loc(
            df=df,
            result=MaterialQuantityOne.OTHER.value,
            and_filters=[
                all_filters.get("insulation_cat_mat_two"),
            ],
            or_filters=[
                all_filters.get("gyp_board_cat_mat_four"),
                all_filters.get("ins_metal_cat_mat_four"),
            ],
        )
        return df


class GypsumMaterialQuantityOne(AbstractFilter):
    """Method to update MQ_1 column for Gypsum entries."""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        df.loc[all_filters.get("plaster_cat_mat_two"), self.column_name_to_change] = (
            MaterialQuantityOne.GYPSUM.value
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityOne.GYPSUM.value,
            and_filters=[
                all_filters.get("insulation_cat_mat_two"),
                all_filters.get("foil_facing_cat_mat_three"),
                all_filters.get("gyp_board_cat_mat_four"),
            ],
        )
        return df


class FireproofMaterialQuantityOne(AbstractFilter):
    """Method to update MQ_1 column for Fireproof entries."""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        df.loc[all_filters.get("fireproof_cat_mat_two"), self.column_name_to_change] = (
            MaterialQuantityOne.FIREPROOF.value
        )
        return df


class DoorFrameMaterialQuantityOneOther(AbstractFilter):
    """
    Method to update MQ_1 column for Doors and frames entries.
    This must be implemented after the first set of MQ_1 values are run.
    """

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_or_loc(
            df=df,
            result=MaterialQuantityOne.DOOR_FRAME.value,
            and_filters=[
                all_filters.get("other_mq_one"),
            ],
            or_filters=[
                all_filters.get("door_cat_mat_two"),
                all_filters.get("opening_hardware_cat_mat_two"),
            ],
        )
        df.loc[all_filters.get("door_cat_ele_four"), self.column_name_to_change] = (
            MaterialQuantityOne.DOOR_FRAME.value
        )
        return df


class WindowFrameMaterialQuantityOneOther(AbstractFilter):
    """
    Method to update MQ_1 column for Window frames entries.
    This must be implemented after the first set of MQ_1 values are run.
    """

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_or_loc(
            df=df,
            result=MaterialQuantityOne.WINDOW_FRAME.value,
            and_filters=[all_filters.get("other_mq_one")],
            or_filters=[
                all_filters.get("window_frame_cat_ele_four"),
                all_filters.get("mullion_cat_ele_four"),
            ],
        )
        return df


class AcousticCeilingsMaterialQuantityOneOther(AbstractFilter):
    """
    Method to update MQ_1 column for Acoustic ceiling entries.
    This must be implemented after the first set of MQ_1 values are run.
    """

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=MaterialQuantityOne.ACOUSTIC_CEILINGS.value,
            and_filters=[
                all_filters.get("other_mq_one"),
                all_filters.get("ceil_sys_cat_ele_four"),
            ],
        )
        return df


class SyntheticCompositesMaterialQuantityOneOther(AbstractFilter):
    """
    Method to update MQ_1 column for Sythetic Composites entries.
    This must be implemented after the first set of MQ_1 values are run.
    """

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_or_loc(
            df=df,
            result=MaterialQuantityOne.SYNTH_COMP.value,
            and_filters=[
                all_filters.get("other_mq_one"),
            ],
            or_filters=[
                all_filters.get("composite_cat_mat_two"),
                all_filters.get("plastic_cat_mat_two"),
            ],
        )
        return df


class CladdingMaterialQuantityOneOther(AbstractFilter):
    """
    Method to update MQ_1 column for Cladding entries.
    This must be implemented after the first set of MQ_1 values are run.
    """

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=MaterialQuantityOne.CLADDING.value,
            and_filters=[
                all_filters.get("other_mq_one"),
                all_filters.get("cladding_cat_mat_two"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityOne.CLADDING.value,
            and_filters=[
                all_filters.get("other_mq_one"),
                all_filters.get("masonry_cat_mat_two"),
                all_filters.get("terracotta_cat_mat_three"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityOne.CLADDING.value,
            and_filters=[
                all_filters.get("other_mq_one"),
            ],
            or_filters=[
                all_filters.get("ins_metal_cat_mat_four"),
                all_filters.get("metal_wall_cat_mat_four"),
                all_filters.get("metal_roofing_cat_mat_four"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityOne.OTHER.value,
            and_filters=[
                all_filters.get("other_mq_one"),
                all_filters.get("ins_metal_cat_mat_four"),
                all_filters.get("fastener_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityOne.OTHER.value,
            and_filters=[
                all_filters.get("other_mq_one"),
                all_filters.get("metal_wall_cat_mat_four"),
                all_filters.get("fastener_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityOne.OTHER.value,
            and_filters=[
                all_filters.get("other_mq_one"),
                all_filters.get("metal_roofing_cat_mat_four"),
                all_filters.get("fastener_cat_mat_three"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityOne.CLADDING.value,
            and_filters=[
                all_filters.get("other_mq_one"),
            ],
            or_filters=[
                all_filters.get("stucco_cat_mat_three"),
                all_filters.get("alum_faced_comp_cat_mat_three"),
            ],
        )
        return df


class AdhesivesMaterialQuantityOneOther(AbstractFilter):
    """
    Method to update MQ_1 column for Adhesives and sealant entries.
    This must be implemented after the first set of MQ_1 values are run.
    """

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_or_loc(
            df=df,
            result=MaterialQuantityOne.ADHES_SEAL.value,
            and_filters=[
                all_filters.get("other_mq_one"),
            ],
            or_filters=[
                all_filters.get("adhesive_cat_mat_two"),
                all_filters.get("sealant_cat_mat_two"),
            ],
        )
        return df


class AirVaporMaterialQuantityOneOther(AbstractFilter):
    """
    Method to update MQ_1 column for Air and vapor barriers entries.
    This must be implemented after the first set of MQ_1 values are run.
    """

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=MaterialQuantityOne.AIR_VAPOR.value,
            and_filters=[
                all_filters.get("other_mq_one"),
                all_filters.get("vapor_barrier_cat_mat_two"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityOne.OTHER.value,
            and_filters=[
                all_filters.get("other_mq_one"),
                all_filters.get("vapor_barrier_cat_mat_two"),
            ],
            or_filters=[
                all_filters.get("roof_cat_mat_three"),
                all_filters.get("roof_start_cat_mat_three"),
            ],
        )
        return df


class CoatingsMaterialQuantityOneOther(AbstractFilter):
    """
    Method to update MQ_1 column for coating entries.
    This must be implemented after the first set of MQ_1 values are run.
    """

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=MaterialQuantityOne.COATINGS.value,
            and_filters=[
                all_filters.get("other_mq_one"),
                all_filters.get("coating_cat_mat_two"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityOne.COATINGS.value,
            and_filters=[
                all_filters.get("other_mq_one"),
                all_filters.get("paint_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityOne.OTHER.value,
            and_filters=[
                all_filters.get("other_mq_one"),
                all_filters.get("paint_cat_mat_three"),
                all_filters.get("fireproof_cat_mat_two"),
            ],
        )
        return df


class FloorTileMaterialQuantityOneOther(AbstractFilter):
    """
    Method to update MQ_1 column for flooring and tile entries.
    This must be implemented after the first set of MQ_1 values are run.
    """

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_or_loc(
            df=df,
            result=MaterialQuantityOne.FLOOR.value,
            and_filters=[
                all_filters.get("other_mq_one"),
            ],
            or_filters=[
                all_filters.get("floor_tile_cat_mat_two"),
                all_filters.get("trim_rubber_cat_mat_three"),
            ],
        )
        return df


class OtherMetalsMaterialQuantityOneOther(AbstractFilter):
    """
    Method to update MQ_1 column for other metals entries.
    This must be implemented after the first set of MQ_1 values are run.
    """

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_or_loc(
            df=df,
            result=MaterialQuantityOne.OTH_METALS.value,
            and_filters=[
                all_filters.get("other_mq_one"),
                all_filters.get("metal_cat_mat_two"),
            ],
            or_filters=[
                all_filters.get("brass_cat_mat_three"),
                all_filters.get("bronze_cat_mat_three"),
                all_filters.get("copper_cat_mat_three"),
                all_filters.get("titanium_cat_mat_three"),
                all_filters.get("zinc_cat_mat_three"),
                all_filters.get("fastener_cat_mat_three"),
            ],
        )
        return df


class WallCoveringsMaterialQuantityOneOther(AbstractFilter):
    """
    Method to update MQ_1 column for Wall Coverings entries.
    This must be implemented after the first set of MQ_1 values are run.
    """

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=MaterialQuantityOne.WALL_COVERINGS.value,
            and_filters=[
                all_filters.get("other_mq_one"),
                all_filters.get("wall_cover_cat_mat_two"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityOne.CLADDING.value,
            and_filters=[
                all_filters.get("other_mq_one"),
                all_filters.get("wall_cover_cat_mat_two"),
                all_filters.get("stucco_cat_mat_three"),
            ],
        )
        return df


# MQ_2 Filters


class ConcreteMaterialQuantityTwo(AbstractFilter):
    """Method to update MQ_2 column for Aluminum entries."""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.READY_MIX_OTHER.value,
            and_filters=[
                all_filters.get("conc_mq_one"),
                all_filters.get("cip_cat_ele_four"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.READY_MIX_LW_3.value,
            and_filters=[
                all_filters.get("conc_mq_one"),
                all_filters.get("cip_cat_ele_four"),
            ],
            or_filters=[
                all_filters.get("cip_lw_3000_cat_mat_four"),
                all_filters.get("cip_lw_3000_cat_mat_four_alt1"),
                all_filters.get("cip_lw_3000_cat_mat_four_alt2"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.READY_MIX_LW_4.value,
            and_filters=[
                all_filters.get("conc_mq_one"),
                all_filters.get("cip_cat_ele_four"),
            ],
            or_filters=[
                all_filters.get("cip_lw_4000_cat_mat_four"),
                all_filters.get("cip_lw_4000_cat_mat_four_alt1"),
                all_filters.get("cip_lw_4000_cat_mat_four_alt2"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.READY_MIX_LW_5.value,
            and_filters=[
                all_filters.get("conc_mq_one"),
                all_filters.get("cip_cat_ele_four"),
            ],
            or_filters=[
                all_filters.get("cip_lw_5000_cat_mat_four"),
                all_filters.get("cip_lw_5000_cat_mat_four_alt1"),
                all_filters.get("cip_lw_5000_cat_mat_four_alt2"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.READY_MIX_NW_2_5.value,
            and_filters=[
                all_filters.get("conc_mq_one"),
                all_filters.get("cip_cat_ele_four"),
            ],
            or_filters=[
                all_filters.get("cip_nw_2500_cat_mat_four"),
                all_filters.get("cip_nw_2500_cat_mat_four_alt1"),
                all_filters.get("cip_nw_2500_cat_mat_four_alt2"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.READY_MIX_NW_3.value,
            and_filters=[
                all_filters.get("conc_mq_one"),
                all_filters.get("cip_cat_ele_four"),
            ],
            or_filters=[
                all_filters.get("cip_nw_3000_cat_mat_four"),
                all_filters.get("cip_nw_3000_cat_mat_four_alt1"),
                all_filters.get("cip_nw_3000_cat_mat_four_alt2"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.READY_MIX_NW_4.value,
            and_filters=[
                all_filters.get("conc_mq_one"),
                all_filters.get("cip_cat_ele_four"),
            ],
            or_filters=[
                all_filters.get("cip_nw_4000_cat_mat_four"),
                all_filters.get("cip_nw_4000_cat_mat_four_alt1"),
                all_filters.get("cip_nw_4000_cat_mat_four_alt2"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.READY_MIX_NW_5.value,
            and_filters=[
                all_filters.get("conc_mq_one"),
                all_filters.get("cip_cat_ele_four"),
            ],
            or_filters=[
                all_filters.get("cip_nw_5000_cat_mat_four"),
                all_filters.get("cip_nw_5000_cat_mat_four_alt1"),
                all_filters.get("cip_nw_5000_cat_mat_four_alt2"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.READY_MIX_NW_6.value,
            and_filters=[
                all_filters.get("conc_mq_one"),
                all_filters.get("cip_cat_ele_four"),
            ],
            or_filters=[
                all_filters.get("cip_nw_6000_cat_mat_four"),
                all_filters.get("cip_nw_6000_cat_mat_four_alt1"),
                all_filters.get("cip_nw_6000_cat_mat_four_alt2"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.READY_MIX_NW_8.value,
            and_filters=[
                all_filters.get("conc_mq_one"),
                all_filters.get("cip_cat_ele_four"),
            ],
            or_filters=[
                all_filters.get("cip_nw_8000_cat_mat_four"),
                all_filters.get("cip_nw_8000_cat_mat_four_alt1"),
                all_filters.get("cip_nw_8000_cat_mat_four_alt2"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.PRECAST.value,
            and_filters=[
                all_filters.get("conc_mq_one"),
                all_filters.get("conc_cat_mat_two"),
                all_filters.get("precast_cat_ele_four"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.GFRC.value,
            and_filters=[
                all_filters.get("conc_mq_one"),
                all_filters.get("gfrc_cat_mat_three"),
            ],
        )
        return df


class SteelMaterialQuantityTwo(AbstractFilter):
    """Method to update MQ_2 column for Glazing entries."""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.HOT_ROLLED.value,
            and_filters=[
                all_filters.get("steel_mq_one"),
            ],
            or_filters=[
                all_filters.get("hot_rolled_cat_mat_five"),
                all_filters.get("hot_rolled_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.HSS.value,
            and_filters=[
                all_filters.get("steel_mq_one"),
                all_filters.get("cold_formed_cat_mat_five"),
                all_filters.get("hss_cat_mat_four"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.STEEL_SHEET.value,
            and_filters=[
                all_filters.get("steel_mq_one"),
                all_filters.get("sheet_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.PLATE.value,
            and_filters=[
                all_filters.get("steel_mq_one"),
                all_filters.get("steel_cat_mat_four"),
                all_filters.get("plate_cat_mat_four"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.OTHER.value,
            and_filters=[
                all_filters.get("steel_mq_one"),
                all_filters.get("steel_cat_mat_four"),
                all_filters.get("plate_cat_mat_four"),
                all_filters.get("quarter_in_cat_mat_five"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.COLD_FORMED.value,
            and_filters=[
                all_filters.get("steel_mq_one"),
                all_filters.get("cold_formed_cat_mat_five"),
                all_filters.get("stud_cat_mat_four"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.DECK.value,
            and_filters=[
                all_filters.get("steel_mq_one"),
                all_filters.get("cold_formed_cat_mat_five"),
                all_filters.get("deck_cat_mat_four"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.REBAR.value,
            and_filters=[
                all_filters.get("steel_mq_one"),
            ],
            or_filters=[
                all_filters.get("reinf_rod_cat_mat_three"),
                all_filters.get("reinf_cmc_cat_mat_three"),
                all_filters.get("alt_reinf_cmc_cat_mat_three"),
                all_filters.get("reinf_csri_cat_mat_three"),
                all_filters.get("alt_reinf_csri_cat_mat_three"),
                all_filters.get("reinf_weld_w_cat_mat_three"),
                all_filters.get("reinf_woven_w_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.REBAR.value,
            and_filters=[
                all_filters.get("steel_mq_one"),
                all_filters.get("steel_cable_cat_mat_three"),
                all_filters.get("pr_conc_bm_cat_mat_four"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.OPEN_WEB_JOISTS.value,
            and_filters=[
                all_filters.get("steel_mq_one"),
                all_filters.get("joist_cat_mat_three"),
            ],
        )
        return df


class MasonryMaterialQuantityTwo(AbstractFilter):
    """Method to update MQ_2 column for Gypsum entries."""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.CMU.value,
            and_filters=[
                all_filters.get("masonry_mq_one"),
                all_filters.get("cmu_cat_ele_four"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.OTHER.value,
            and_filters=[
                all_filters.get("masonry_mq_one"),
                all_filters.get("cmu_cat_ele_four"),
            ],
            or_filters=[
                all_filters.get("mortar_cat_mat_three"),
                all_filters.get("grout_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.BRICK.value,
            and_filters=[
                all_filters.get("masonry_mq_one"),
                all_filters.get("brick_cat_ele_four"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.OTHER.value,
            and_filters=[
                all_filters.get("masonry_mq_one"),
                all_filters.get("brick_cat_ele_four"),
            ],
            or_filters=[
                all_filters.get("mortar_cat_mat_three"),
                all_filters.get("grout_cat_mat_three"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.STONE.value,
            and_filters=[
                all_filters.get("masonry_mq_one"),
            ],
            or_filters=[
                all_filters.get("stone_cat_ele_four"),
                all_filters.get("stone_cat_mat_two"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.OTHER.value,
            and_filters=[
                all_filters.get("masonry_mq_one"),
                all_filters.get("stone_cat_ele_four"),
            ],
            or_filters=[
                all_filters.get("mortar_cat_mat_three"),
                all_filters.get("grout_cat_mat_three"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.OTHER.value,
            and_filters=[
                all_filters.get("masonry_mq_one"),
                all_filters.get("stone_cat_mat_two"),
            ],
            or_filters=[
                all_filters.get("mortar_cat_mat_three"),
                all_filters.get("grout_cat_mat_three"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.GROUT.value,
            and_filters=[
                all_filters.get("masonry_mq_one"),
            ],
            or_filters=[
                all_filters.get("mortar_cat_mat_three"),
                all_filters.get("grout_cat_mat_three"),
            ],
        )
        return df


class AluminumMaterialQuantityTwo(AbstractFilter):
    """Method to update MQ_2 column for Insulation entries."""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.EXTRUSION.value,
            and_filters=[
                all_filters.get("alum_mq_one"),
                all_filters.get("extru_cat_mat_three"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.ALUM_SHEET.value,
            and_filters=[
                all_filters.get("alum_mq_one"),
            ],
            or_filters=[
                all_filters.get("sheet_cat_mat_three"),
            ],
        )
        return df


class WoodMaterialQuantityTwo(AbstractFilter):
    """Method to update MQ_2 column for Roofing entries."""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.HEAVY_TIMBER.value,
            and_filters=[
                all_filters.get("wood_mq_one"),
                all_filters.get("heavy_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.WOOD_FRAMING.value,
            and_filters=[
                all_filters.get("wood_mq_one"),
                all_filters.get("soft_cat_mat_three"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.HARDWOOD.value,
            and_filters=[
                all_filters.get("wood_mq_one"),
            ],
            or_filters=[
                all_filters.get("hardwood_cat_mat_three"),
                all_filters.get("lumber_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.PLYWOOD.value,
            and_filters=[
                all_filters.get("wood_mq_one"),
                all_filters.get("plywood_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.OSB.value,
            and_filters=[
                all_filters.get("wood_mq_one"),
                all_filters.get("osb_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.MDF.value,
            and_filters=[
                all_filters.get("wood_mq_one"),
                all_filters.get("mdf_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.PSL.value,
            and_filters=[
                all_filters.get("wood_mq_one"),
                all_filters.get("psl_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.GLT.value,
            and_filters=[
                all_filters.get("wood_mq_one"),
                all_filters.get("glulam_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.CLT.value,
            and_filters=[
                all_filters.get("wood_mq_one"),
                all_filters.get("clt_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.WOOD_I_JOIST.value,
            and_filters=[
                all_filters.get("wood_mq_one"),
                all_filters.get("i_joist_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.LSL.value,
            and_filters=[
                all_filters.get("wood_mq_one"),
                all_filters.get("lsl_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.LVL.value,
            and_filters=[
                all_filters.get("wood_mq_one"),
                all_filters.get("lvl_cat_mat_three"),
            ],
        )
        return df


class GlazingMaterialQuantityTwo(AbstractFilter):
    """Method to update MQ_2 column for Glazing entries."""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.IGU.value,
            and_filters=[
                all_filters.get("glazing_mq_one"),
                all_filters.get("igu_cat_mat_four"),
            ],
        )
        return df


class GypsumMaterialQuantityTwo(AbstractFilter):
    """Method to update MQ_2 column for Gypsum entries."""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        df.loc[all_filters.get("gypsum_mq_one"), self.column_name_to_change] = (
            MaterialQuantityTwo.INT_GYPSUM.value
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.GLASSMAT_SHEATHING.value,
            and_filters=[
                all_filters.get("gypsum_mq_one"),
                all_filters.get("fib_glass_cat_mat_three"),
            ],
        )
        return df


class InsulationMaterialQuantityTwo(AbstractFilter):
    """Method to update MQ_2 column for Insulation entries."""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.XPS.value,
            and_filters=[
                all_filters.get("insulation_mq_one"),
                all_filters.get("xps_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.PIR.value,
            and_filters=[
                all_filters.get("insulation_mq_one"),
                all_filters.get("pir_cat_mat_three"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.MIN_WOOL_LOW.value,
            and_filters=[
                all_filters.get("insulation_mq_one"),
                all_filters.get("min_wool_cat_mat_three"),
            ],
            or_filters=[
                all_filters.get("low_cat_mat_three"),
                all_filters.get("ecose_cat_mat_three"),
                all_filters.get("115_cat_mat_three"),
                all_filters.get("132_cat_mat_three"),
                all_filters.get("135_cat_mat_three"),
                all_filters.get("140_cat_mat_three"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.MIN_WOOL_HIGH.value,
            and_filters=[
                all_filters.get("insulation_mq_one"),
                all_filters.get("min_wool_cat_mat_three"),
            ],
            or_filters=[
                all_filters.get("high_cat_mat_three"),
                all_filters.get("ddp_cat_mat_three"),
                all_filters.get("432_cat_mat_three"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.FIB_BLANKET.value,
            and_filters=[
                all_filters.get("insulation_mq_one"),
            ],
            or_filters=[
                all_filters.get("fiberglass_cat_mat_three"),
                all_filters.get("glass_fiber_cat_mat_three"),
                all_filters.get("glass_wool_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.CELLULOSE.value,
            and_filters=[
                all_filters.get("insulation_mq_one"),
                all_filters.get("cellulose_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.EPS.value,
            and_filters=[
                all_filters.get("insulation_mq_one"),
                all_filters.get("eps_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.POLY_FOAM.value,
            and_filters=[
                all_filters.get("insulation_mq_one"),
                all_filters.get("spray_cat_mat_three"),
            ],
        )
        return df


class RoofMaterialQuantityTwo(AbstractFilter):
    """Method to update MQ_2 column for Roofing entries."""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.BITUMEN.value,
            and_filters=[
                all_filters.get("roofing_mq_one"),
                all_filters.get("mod_bitumen_cat_mat_three"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.BUR.value,
            and_filters=[
                all_filters.get("roofing_mq_one"),
            ],
            or_filters=[
                all_filters.get("built_up_cat_mat_three"),
                all_filters.get("bur_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.TPO.value,
            and_filters=[
                all_filters.get("roofing_mq_one"),
                all_filters.get("tpo_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.EPDM.value,
            and_filters=[
                all_filters.get("roofing_mq_one"),
                all_filters.get("epdm_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.PVC.value,
            and_filters=[
                all_filters.get("roofing_mq_one"),
                all_filters.get("PVC_cat_mat_three"),
            ],
        )
        return df


class FireproofMaterialQuantityTwo(AbstractFilter):
    """Method to update MQ_2 column for Fireproof entries."""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.CEMENTITIOUS.value,
            and_filters=[
                all_filters.get("fireproof_mq_one"),
                all_filters.get("cementitious_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.INTUMESCENT.value,
            and_filters=[
                all_filters.get("fireproof_mq_one"),
                all_filters.get("intumescent_cat_mat_three"),
            ],
        )
        return df


class DoorFrameMaterialQuantityTwoOther(AbstractFilter):
    """
    Method to update MQ_2 column for Doors and frames entries.
    This must be implemented after the first set of MQ_2 values are run.
    """

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.ALUM_DOOR.value,
            and_filters=[
                all_filters.get("doors_and_frames_mq_one"),
                all_filters.get("door_cat_mat_two"),
                all_filters.get("aluminum_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.ALUM_DOOR_FRAME.value,
            and_filters=[
                all_filters.get("doors_and_frames_mq_one"),
                all_filters.get("door_frame_cat_mat_two"),
                all_filters.get("aluminum_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.WOOD_DOOR.value,
            and_filters=[
                all_filters.get("doors_and_frames_mq_one"),
                all_filters.get("door_cat_mat_two"),
                all_filters.get("wood_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.WOOD_DOOR_FRAME.value,
            and_filters=[
                all_filters.get("doors_and_frames_mq_one"),
                all_filters.get("door_frame_cat_mat_two"),
                all_filters.get("wood_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.STEEL_DOOR.value,
            and_filters=[
                all_filters.get("doors_and_frames_mq_one"),
                all_filters.get("door_cat_mat_two"),
                all_filters.get("hollow_cat_mat_three"),
                all_filters.get("steel_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.STEEL_DOOR_FRAME.value,
            and_filters=[
                all_filters.get("doors_and_frames_mq_one"),
                all_filters.get("door_frame_cat_mat_two"),
                all_filters.get("galvanized_cat_mat_three"),
            ],
        )
        return df


class WindowFrameMaterialQuantityTwoOther(AbstractFilter):
    """
    Method to update MQ_2 column for Window frames entries.
    This must be implemented after the first set of MQ_2 values are run.
    """

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.ALUM_WINDOW.value,
            and_filters=[
                all_filters.get("window_frame_mq_one"),
            ],
            or_filters=[
                all_filters.get("aluminum_cat_mat_three"),
                all_filters.get("aluminum_cat_mat_five"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.OTHER.value,
            and_filters=[
                all_filters.get("window_frame_mq_one"),
                all_filters.get("mullion_cat_ele_four"),
            ],
            or_filters=[
                all_filters.get("aluminum_cat_mat_three"),
                all_filters.get("aluminum_cat_mat_five"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.CW_MULLION.value,
            and_filters=[
                all_filters.get("window_frame_mq_one"),
                all_filters.get("mullion_cat_ele_four"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.STEEL_WINDOW.value,
            and_filters=[
                all_filters.get("window_frame_mq_one"),
                all_filters.get("steel_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.VINYL_WINDOW.value,
            and_filters=[
                all_filters.get("window_frame_mq_one"),
                all_filters.get("vinyl_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.WOOD_WINDOW.value,
            and_filters=[
                all_filters.get("window_frame_mq_one"),
                all_filters.get("wood_cat_mat_three"),
            ],
        )
        return df


class AcousticCeilingsMaterialQuantityTwoOther(AbstractFilter):
    """
    Method to update MQ_2 column for Acoustic ceiling entries.
    This must be implemented after the first set of MQ_2 values are run.
    """

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.ACOUS_CEIL_FIBER.value,
            and_filters=[
                all_filters.get("acous_ceilings_mq_one"),
                all_filters.get("ceil_tile_cat_mat_two"),
                all_filters.get("ceil_tile_cat_mat_three"),
                all_filters.get("fiber_cat_mat_three"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.ACOUS_CEIL_ALUM.value,
            and_filters=[
                all_filters.get("acous_ceilings_mq_one"),
                all_filters.get("ceil_tile_cat_mat_three"),
                all_filters.get("aluminum_cat_mat_three"),
            ],
            or_filters=[
                all_filters.get("ceil_tile_cat_mat_two"),
                all_filters.get("metal_coating_cat_mat_two"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.ACOUS_CEIL_STEEL.value,
            and_filters=[
                all_filters.get("acous_ceilings_mq_one"),
                all_filters.get("ceil_tile_cat_mat_three"),
                all_filters.get("steel_cat_mat_three"),
            ],
            or_filters=[
                all_filters.get("ceil_tile_cat_mat_two"),
                all_filters.get("metal_coating_cat_mat_two"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.SUSP_SYS.value,
            and_filters=[
                all_filters.get("acous_ceilings_mq_one"),
                all_filters.get("ceil_tile_cat_mat_two"),
                all_filters.get("suspended_cat_mat_three"),
            ],
        )
        return df


class SyntheticCompositesMaterialQuantityTwoOther(AbstractFilter):
    """
    Method to update MQ_2 column for Sythetic Composites entries.
    This must be implemented after the first set of MQ_2 values are run.
    """

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        return df


class CladdingMaterialQuantityTwoOther(AbstractFilter):
    """
    Method to update MQ_2 column for Composite panel entries.
    This must be implemented after the first set of MQ_2 values are run.
    """

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.ACM.value,
            and_filters=[
                all_filters.get("cladding_mq_one"),
                all_filters.get("alum_faced_comp_cat_mat_three"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.ALUM_METAL_PANEL.value,
            and_filters=[
                all_filters.get("cladding_mq_one"),
                all_filters.get("aluminum_cat_mat_three"),
            ],
            or_filters=[
                all_filters.get("metal_wall_cat_mat_four"),
                all_filters.get("siding_cat_mat_four"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.OTHER.value,
            and_filters=[
                all_filters.get("cladding_mq_one"),
                all_filters.get("insulated_cat_mat_three"),
                all_filters.get("aluminum_cat_mat_three"),
            ],
            or_filters=[
                all_filters.get("metal_wall_cat_mat_four"),
                all_filters.get("siding_cat_mat_four"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.STEEL_METAL_PANEL.value,
            and_filters=[
                all_filters.get("cladding_mq_one"),
                all_filters.get("steel_cat_mat_three"),
            ],
            or_filters=[
                all_filters.get("metal_wall_cat_mat_four"),
                all_filters.get("siding_cat_mat_four"),
                all_filters.get("metal_roofing_cat_mat_four"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.OTHER.value,
            and_filters=[
                all_filters.get("cladding_mq_one"),
                all_filters.get("insulated_cat_mat_three"),
                all_filters.get("steel_cat_mat_three"),
            ],
            or_filters=[
                all_filters.get("metal_wall_cat_mat_four"),
                all_filters.get("siding_cat_mat_four"),
                all_filters.get("metal_roofing_cat_mat_four"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.ARCH_FIBER_PANEL.value,
            and_filters=[
                all_filters.get("cladding_mq_one"),
                all_filters.get("fiber_cem_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.IMP.value,
            and_filters=[
                all_filters.get("cladding_mq_one"),
                all_filters.get("ins_metal_cat_mat_four"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.TERRACOTTA.value,
            and_filters=[
                all_filters.get("cladding_mq_one"),
                all_filters.get("masonry_cat_mat_two"),
                all_filters.get("terracotta_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.STUCCO.value,
            and_filters=[
                all_filters.get("cladding_mq_one"),
                all_filters.get("stucco_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.GFRC_PANEL.value,
            and_filters=[
                all_filters.get("cladding_mq_one"),
                all_filters.get("gfrc_cat_mat_four"),
                all_filters.get("panel_cat_mat_four"),
            ],
        )

        return df


class AdhesivesMaterialQuantityTwoOther(AbstractFilter):
    """
    Method to update MQ_2 column for Adhesives and sealant entries.
    This must be implemented after the first set of MQ_2 values are run.
    """

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        return df


class AirVaporMaterialQuantityTwoOther(AbstractFilter):
    """
    Method to update MQ_2 column for Air and vapor barriers entries.
    This must be implemented after the first set of MQ_2 values are run.
    """

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        return df


class CoatingsMaterialQuantityTwoOther(AbstractFilter):
    """
    Method to update MQ_2 column for Air and vapor barriers entries.
    This must be implemented after the first set of MQ_2 values are run.
    """

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.PAINT.value,
            and_filters=[
                all_filters.get("coatings_mq_one"),
                all_filters.get("paint_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.OTHER.value,
            and_filters=[
                all_filters.get("coatings_mq_one"),
                all_filters.get("paint_cat_mat_three"),
                all_filters.get("fireproof_cat_mat_two"),
            ],
        )
        return df


class FloorTileMaterialQuantityTwoOther(AbstractFilter):
    """
    Method to update MQ_2 column for flooring and tile entries.
    This must be implemented after the first set of MQ_2 values are run.
    """

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.CARPET.value,
            and_filters=[
                all_filters.get("floor_tile_mq_one"),
                all_filters.get("carpet_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.RES_FLOOR_VINYL.value,
            and_filters=[
                all_filters.get("floor_tile_mq_one"),
                all_filters.get("vinyl_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.RES_FLOOR_VINYL.value,
            and_filters=[
                all_filters.get("floor_tile_mq_one"),
                all_filters.get("rubber_cat_mat_three"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=MaterialQuantityTwo.PORCELAIN_TILE.value,
            and_filters=[
                all_filters.get("floor_tile_mq_one"),
            ],
            or_filters=[
                all_filters.get("ceramic_cat_mat_three"),
                all_filters.get("porcelain_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.STONE_TILE.value,
            and_filters=[
                all_filters.get("floor_tile_mq_one"),
                all_filters.get("stone_tile_cat_mat_four"),
            ],
        )
        return df


class OtherMetalsMaterialQuantityTwoOther(AbstractFilter):
    """
    Method to update MQ_2 column for other metals entries.
    This must be implemented after the first set of MQ_2 values are run.
    """

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.BRASS.value,
            and_filters=[
                all_filters.get("other_metals_mq_one"),
                all_filters.get("brass_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.BRONZE.value,
            and_filters=[
                all_filters.get("other_metals_mq_one"),
                all_filters.get("bronze_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.COPPER.value,
            and_filters=[
                all_filters.get("other_metals_mq_one"),
                all_filters.get("copper_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.TITANIUM.value,
            and_filters=[
                all_filters.get("other_metals_mq_one"),
                all_filters.get("titanium_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.ZINC.value,
            and_filters=[
                all_filters.get("other_metals_mq_one"),
                all_filters.get("zinc_cat_mat_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.FASTENERS.value,
            and_filters=[
                all_filters.get("other_metals_mq_one"),
                all_filters.get("fastener_cat_mat_three"),
            ],
        )
        return df


class FinalOtherMaterialQuantityTwoOther(AbstractFilter):
    """
    Method to update MQ_2 column for other entries.
    This must be implemented after the first set of MQ_2 values are run.
    The purpose of this filter is rename MQ_2 values to other values
    based on the MQ_1 value
    """

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.CONCRETE_OTHER.value,
            and_filters=[
                all_filters.get("conc_mq_one"),
                all_filters.get("other_mq_two"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.STEEL_OTHER.value,
            and_filters=[
                all_filters.get("steel_mq_one"),
                all_filters.get("other_mq_two"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.MASONRY_OTHER.value,
            and_filters=[
                all_filters.get("masonry_mq_one"),
                all_filters.get("other_mq_two"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.ALUM_OTHER.value,
            and_filters=[
                all_filters.get("alum_mq_one"),
                all_filters.get("other_mq_two"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.WOOD_OTHER.value,
            and_filters=[
                all_filters.get("wood_mq_one"),
                all_filters.get("other_mq_two"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.GLAZING_OTHER.value,
            and_filters=[
                all_filters.get("glazing_mq_one"),
                all_filters.get("other_mq_two"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.INSULATION_OTHER.value,
            and_filters=[
                all_filters.get("insulation_mq_one"),
                all_filters.get("other_mq_two"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.GYPSUM_OTHER.value,
            and_filters=[
                all_filters.get("gypsum_mq_one"),
                all_filters.get("other_mq_two"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.ROOFING_OTHER.value,
            and_filters=[
                all_filters.get("roofing_mq_one"),
                all_filters.get("other_mq_two"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.FIREPROOFING_OTHER.value,
            and_filters=[
                all_filters.get("fireproof_mq_one"),
                all_filters.get("other_mq_two"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.DOOR_OTHER.value,
            and_filters=[
                all_filters.get("doors_and_frames_mq_one"),
                all_filters.get("other_mq_two"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.WINDOW_OTHER.value,
            and_filters=[
                all_filters.get("window_frame_mq_one"),
                all_filters.get("other_mq_two"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.ACOUS_CEIL_OTHER.value,
            and_filters=[
                all_filters.get("acous_ceilings_mq_one"),
                all_filters.get("other_mq_two"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.SYNTH_COMP.value,
            and_filters=[
                all_filters.get("synth_comp_mq_one"),
                all_filters.get("other_mq_two"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.CLADDING_OTHER.value,
            and_filters=[
                all_filters.get("cladding_mq_one"),
                all_filters.get("other_mq_two"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.ADHES_SEAL.value,
            and_filters=[
                all_filters.get("adhes_seal_mq_one"),
                all_filters.get("other_mq_two"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.AIR_VAPOR.value,
            and_filters=[
                all_filters.get("vapor_barrier_mq_one"),
                all_filters.get("other_mq_two"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.COATING_OTHER.value,
            and_filters=[
                all_filters.get("coatings_mq_one"),
                all_filters.get("other_mq_two"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.FLOOR_OTHER.value,
            and_filters=[
                all_filters.get("floor_tile_mq_one"),
                all_filters.get("other_mq_two"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.OTH_METAL_OTHER.value,
            and_filters=[
                all_filters.get("other_metals_mq_one"),
                all_filters.get("other_mq_two"),
            ],
        )
        self.and_loc(
            df=df,
            result=MaterialQuantityTwo.WALL_COVERINGS.value,
            and_filters=[
                all_filters.get("wall_coverings_mq_one"),
                all_filters.get("other_mq_two"),
            ],
        )
        return df

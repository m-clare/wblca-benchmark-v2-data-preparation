# pylint: disable=C0103, W0718
"""Defines Tally Filter classes to update values in CLF Omni Column"""
from typing import Dict
import pandas as pd
from wblca_benchmark_v2_data_prep.lca_results.abstract_filters import AbstractFilter
from wblca_benchmark_v2_data_prep.lca_results.enums import \
    OmniClassLevelOne, RevitBuildingCategory


class Ceilings(AbstractFilter):
    """Methods to update CLF Omni column for ceiling entries"""

    def filtering(self, df: pd.DataFrame,
                  all_filters: Dict[str, pd.Series]) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.UNKNOWN.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_ceilings')
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_FINISHES.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_ceilings'),
                all_filters.get('ty_ed_09')
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_CONSTRUCTION.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_ceilings'),
                all_filters.get('ty_ed_09'),
                all_filters.get('ty_ec_steel')
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_ceilings'),
                all_filters.get('ty_ed_08')
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_ceilings'),
                all_filters.get('ty_ed_07')
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_FINISHES.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_ceilings'),
                all_filters.get('ty_ed_06')
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_CONSTRUCTION.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_ceilings'),
                all_filters.get('ty_ed_06')
            ],
            or_filters=[
                all_filters.get('ty_en_wood_framing'),
                all_filters.get('ty_en_part_board'),
                all_filters.get('ty_en_ply_int'),
                all_filters.get('ty_en_mdf'),
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_ceilings'),
                all_filters.get('ty_ed_06'),
            ],
            or_filters=[
                all_filters.get('ty_en_ply_ext'),
                all_filters.get('ty_en_wood_framing_w_ins')
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_FINISHES.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_ceilings'),
                all_filters.get('ty_ed_05'),
            ],
            or_filters=[
                all_filters.get('ty_ec_alum'),
                all_filters.get('ty_ec_ceil_sys')
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_CONSTRUCTION.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_ceilings'),
                all_filters.get('ty_ed_05'),
                all_filters.get('ty_ec_steel')
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_FINISHES.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_ceilings'),
                all_filters.get('ty_ed_05'),
                all_filters.get('ty_ec_steel')
            ],
            or_filters=[
                all_filters.get('ty_en_steel_plate'),
                all_filters.get('ty_en_steel_sheet')
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_ceilings'),
            ],
            or_filters=[
                all_filters.get('ty_ed_04'),
                all_filters.get('ty_ed_03')
            ]
        )
        return df


class CurtainWallPanels(AbstractFilter):
    """Methods to update CLF Omni column for curtain wall panel entries"""
    def filtering(self, df: pd.DataFrame,
                  all_filters: Dict[str, pd.Series]) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.UNKNOWN.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_cw_panels'),
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_cw_panels'),
                all_filters.get('rt_be_enc')
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_CONSTRUCTION.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_cw_panels'),
                all_filters.get('rt_be_int')
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_cw_panels'),
            ],
            or_filters=[
                all_filters.get('ty_ed_05'),
                all_filters.get('ty_ed_07'),
                all_filters.get('ty_ed_08'),
                all_filters.get('rt_fn_louver'),
                all_filters.get('rt_fn_shade'),
                all_filters.get('rt_fn_spandrel'),
                all_filters.get('rt_fn_glaze')
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_CONSTRUCTION.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_cw_panels'),
                all_filters.get('rt_fn_int')
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_FINISHES.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_cw_panels'),
                all_filters.get('ty_ed_09')
            ]
        )
        return df


class CurtainWallMullions(AbstractFilter):
    """Methods to update CLF Omni column for curtain wall mullion entries"""
    def filtering(self, df: pd.DataFrame,
                  all_filters: Dict[str, pd.Series]) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.UNKNOWN.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_cw_mull'),
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_cw_mull'),
            ],
            or_filters=[
                all_filters.get('ty_ed_05'),
                all_filters.get('ty_ed_07'),
                all_filters.get('ty_ed_08'),
                all_filters.get('rt_be_enc'),
                all_filters.get('rt_fn_louver'),
                all_filters.get('rt_fn_shade'),
                all_filters.get('rt_fn_spandrel'),
                all_filters.get('rt_fn_glaze')
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_CONSTRUCTION.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_cw_mull'),
                all_filters.get('rt_be_int')
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_FINISHES.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_cw_mull'),
                all_filters.get('ty_ed_09')
            ]
        )
        return df


class Doors(AbstractFilter):
    """Methods to update CLF Omni column for door entries"""
    def filtering(self, df: pd.DataFrame,
                  all_filters: Dict[str, pd.Series]) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.UNKNOWN.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_door'),
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_door'),
                all_filters.get('rt_be_enc')
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_CONSTRUCTION.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_door'),
                all_filters.get('rt_be_int')
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_door'),

            ],
            or_filters=[
                all_filters.get('ty_en_igu'),
                all_filters.get('ty_en_ext')
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_CONSTRUCTION.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_door'),

            ],
            or_filters=[
                all_filters.get('ty_en_int'),
                all_filters.get('ty_en_toilet')
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_FINISHES.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_door'),
                all_filters.get('ty_ed_06'),
                all_filters.get('ty_en_orn_wood')
            ]
        )
        return df


class Floors(AbstractFilter):
    """Methods to update CLF Omni column for floor entries"""
    def filtering(self, df: pd.DataFrame,
                  all_filters: Dict[str, pd.Series]) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_floor'),
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_floor'),
            ],
            or_filters=[
                all_filters.get('rt_be_sup'),
                all_filters.get('rt_fn_slab'),
                all_filters.get('rt_fn_pt'),
                all_filters.get('rt_fn_topping'),
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.SUBSTRUCTURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_floor'),
                all_filters.get('rt_be_sub')
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.SUBSTRUCTURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_floor'),
                all_filters.get('ty_ed_03')
            ],
            or_filters=[
                all_filters.get('rt_fn_fdn'),
                all_filters.get('rt_fn_ftg'),
                all_filters.get('rt_fn_bsmnt'),
                all_filters.get('rt_fn_stem'),
                all_filters.get('rt_fn_curb'),
                all_filters.get('rt_fn_pile'),
                all_filters.get('rt_fn_pier'),
                all_filters.get('rt_fn_pit'),
                all_filters.get('rt_fn_sog')
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_FINISHES.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_floor'),
                all_filters.get('ty_ed_09')
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_floor'),
                all_filters.get('ty_ed_07')
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_floor'),
            ],
            or_filters=[
                all_filters.get('ty_ed_06'),
                all_filters.get('rt_fn_metal_deck')
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_FINISHES.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_floor'),
                all_filters.get('ty_ed_06'),
            ],
            or_filters=[
                all_filters.get('ty_en_orn_wood'),
                all_filters.get('ty_mg_coating')
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_floor'),
                all_filters.get('ty_ed_06'),
                all_filters.get('ty_mg_insulation')
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_floor'),
                all_filters.get('ty_ed_03')
            ],
            or_filters=[
                all_filters.get('ty_en_cip_custom'),
                all_filters.get('rt_fn_paver')
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_floor'),
                all_filters.get('ty_ed_05'),
                all_filters.get('rt_fn_grate')
            ]
        )
        return df


class Roofs(AbstractFilter):
    """Methods to update CLF Omni column for roof entries"""
    def filtering(self, df: pd.DataFrame,
                  all_filters: Dict[str, pd.Series]) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.UNKNOWN.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_roof'),
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_FINISHES.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_roof'),
                all_filters.get('ty_ed_09'),
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_roof'),
                all_filters.get('ty_ed_09'),
                all_filters.get('ty_mn_fib')
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_roof'),
            ],
            or_filters=[
                all_filters.get('ty_ed_07'),
                all_filters.get('ty_ed_05'),
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_roof'),
            ],
            or_filters=[
                all_filters.get('ty_ed_06'),
                all_filters.get('ty_ed_03'),
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_roof'),
                all_filters.get('ty_ed_05'),
            ],
            or_filters=[
                all_filters.get('ty_ec_alum'),
                all_filters.get('ty_ec_steel')
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_roof'),
                all_filters.get('ty_ed_06'),
            ],
            or_filters=[
                all_filters.get('ty_mg_insulation'),
                all_filters.get('ty_en_fib_ins')
            ]
        )
        return df


class Railings(AbstractFilter):
    """Methods to update CLF Omni column for railing entries"""
    def filtering(self, df: pd.DataFrame,
                  all_filters: Dict[str, pd.Series]) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_railing'),
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_CONSTRUCTION.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_railing'),
                all_filters.get('rt_be_int')
            ]
        )
        return df


class Stairs(AbstractFilter):
    """Methods to update CLF Omni column for stair entries"""
    def filtering(self, df: pd.DataFrame,
                  all_filters: Dict[str, pd.Series]) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_stairs'),
            ]
        )
        return df


class StructuralColumns(AbstractFilter):
    """Methods to update CLF Omni column for structural column entries"""
    def filtering(self, df: pd.DataFrame,
                  all_filters: Dict[str, pd.Series]) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_str_col'),
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_FINISHES.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_str_col'),
                all_filters.get('ty_ed_09')
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_str_col'),
                all_filters.get('ty_ed_07')
            ]
        )
        return df


class StructuralConnections(AbstractFilter):
    """Methods to update CLF Omni column for structural connection entries"""
    def filtering(self, df: pd.DataFrame,
                  all_filters: Dict[str, pd.Series]) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_str_con'),
            ]
        )
        return df


class StructuralFoundations(AbstractFilter):
    """Methods to update CLF Omni column for structural foundation entries"""
    def filtering(self, df: pd.DataFrame,
                  all_filters: Dict[str, pd.Series]) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.SUBSTRUCTURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_str_fdn'),
            ]
        )
        return df


class StructuralFraming(AbstractFilter):
    """Methods to update CLF Omni column for structural framing entries"""
    def filtering(self, df: pd.DataFrame,
                  all_filters: Dict[str, pd.Series]) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_str_frm'),
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_FINISHES.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_str_frm'),
                all_filters.get('ty_ed_09')
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_str_frm'),
                all_filters.get('ty_ed_07')
            ]
        )
        return df


class Walls(AbstractFilter):
    """Methods to update CLF Omni column for wall entries"""
    def filtering(self, df: pd.DataFrame,
                  all_filters: Dict[str, pd.Series]) -> pd.DataFrame:
        # then adjust CLF Omni
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.UNKNOWN.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_wall'),
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_wall'),
                all_filters.get('rt_be_sup')
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.SUBSTRUCTURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_wall'),
                all_filters.get('rt_be_sub')
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_wall'),
                all_filters.get('rt_be_enc')
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_wall'),
            ],
            or_filters=[
                all_filters.get('rt_fn_shear'),
                all_filters.get('ty_ed_03')
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.SUBSTRUCTURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_wall'),
                all_filters.get('ty_ed_03')
            ],
            or_filters=[
                all_filters.get('rt_fn_fdn'),
                all_filters.get('rt_fn_ftg'),
                all_filters.get('rt_fn_bsmnt'),
                all_filters.get('rt_fn_below'),
                all_filters.get('rt_fn_retain'),
                all_filters.get('rt_fn_stem'),
                all_filters.get('rt_fn_site'),
                all_filters.get('rt_fn_cistern'),
                all_filters.get('rt_fn_battered'),
                all_filters.get('rt_fn_caisson'),
                all_filters.get('rt_fn_pile'),
                all_filters.get('rt_fn_pier'),
                all_filters.get('rt_fn_pit'),
                all_filters.get('rt_fn_well')
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_CONSTRUCTION.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_wall'),
            ],
            or_filters=[
                all_filters.get('rt_fn_shaft'),
                all_filters.get('rt_fn_p_naming')
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_wall'),
            ],
            or_filters=[
                all_filters.get('rt_fn_ex'),
                all_filters.get('rt_fn_wall_w'),
                all_filters.get('ty_ed_08'),
                all_filters.get('ty_ed_07')
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_FINISHES.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_wall'),
                all_filters.get('ty_ed_09')
            ]
        )

        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_CONSTRUCTION.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_wall'),
                all_filters.get('rt_be_int'),
                all_filters.get('ty_ed_04')
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_FINISHES.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_wall'),
                all_filters.get('rt_be_int'),
                all_filters.get('ty_ed_05')
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_CONSTRUCTION.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_wall'),
                all_filters.get('rt_be_int'),
                all_filters.get('ty_ed_05'),
                all_filters.get('ty_ec_steel'),
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_FINISHES.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_wall'),
                all_filters.get('rt_be_int'),
                all_filters.get('ty_ed_06')
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_CONSTRUCTION.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_wall'),
                all_filters.get('rt_be_int'),
                all_filters.get('ty_ed_06')
            ],
            or_filters=[
                all_filters.get('ty_en_ply_lvl'),
                all_filters.get('ty_en_ply_int'),
                all_filters.get('ty_en_ply_ext'),
                all_filters.get('ty_en_ply_osb'),
                all_filters.get('ty_en_wood_framing'),
                all_filters.get('ty_en_wood_framing_w_ins')
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_CONSTRUCTION.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_wall'),
                all_filters.get('rt_be_int'),
            ],
            or_filters=[
                all_filters.get('ty_ed_07'),
                all_filters.get('ty_ed_08')
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_FINISHES.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_wall'),
                all_filters.get('rt_be_int'),
                all_filters.get('ty_ed_07'),
                all_filters.get('ty_ec_cladding'),
            ]
        )
        return df


class Windows(AbstractFilter):
    """Methods to update CLF Omni column for window entries"""
    def filtering(self, df: pd.DataFrame,
                  all_filters: Dict[str, pd.Series]) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get('ty_clf_omni_na'),
                all_filters.get('rt_c_window'),
            ]
        )
        return df


def adjust_tally_walls(df: pd.DataFrame) -> pd.DataFrame:
    """Adjusts revit building element values for wall objects in tally entries.

    Args:
        df (pd.DataFrame): DataFrame of Tally entries

    Raises:
        KeyError: raised if loc function does not work due to invalid key

    Returns:
        pd.DataFrame: DataFrame with updated revit building element values
    """
    rt_c_wall = df['Revit category'].str.fullmatch('Walls')

    rt_fn_int = df['Revit family name'].str.contains('int|Int|INT|interior|Interior|INTERIOR')
    rt_fn_ext = df['Revit family name'].str.contains('ext|Ext|EXT|exterior|Exterior|EXTERIOR')
    rt_fn_rainscreen = df['Revit family name'].str.contains('rainscreen|Rainscreen|RAINSCREEN')
    rt_fn_parapet = df['Revit family name'].str.contains('parapet|Parapet|PARAPET')
    rt_fn_soffit = df['Revit family name'].str.contains('soffit|Soffit|SOFFIT')
    rt_fn_partition = df['Revit family name'].str.contains('partition|Partition|PARTITION')
    rt_fn_enc = df['Revit family name'].str.contains(
        'enc|Enc|ENC|enclosure|Enclosure|ENCLOSURE'
    )

    try:
        df.loc[(rt_c_wall) & (rt_fn_ext), 'Revit building element'] = \
            RevitBuildingCategory.ENCLOSURE.value
        df.loc[(rt_c_wall) & (rt_fn_rainscreen), 'Revit building element'] = \
            RevitBuildingCategory.ENCLOSURE.value
        df.loc[(rt_c_wall) & (rt_fn_parapet), 'Revit building element'] = \
            RevitBuildingCategory.ENCLOSURE.value
        df.loc[(rt_c_wall) & (rt_fn_soffit), 'Revit building element'] = \
            RevitBuildingCategory.ENCLOSURE.value
        df.loc[(rt_c_wall) & (rt_fn_enc), 'Revit building element'] = \
            RevitBuildingCategory.ENCLOSURE.value
        df.loc[(rt_c_wall) & (rt_fn_int), 'Revit building element'] = \
            RevitBuildingCategory.INTERIORS.value
        df.loc[(rt_c_wall) & (rt_fn_partition), 'Revit building element'] = \
            RevitBuildingCategory.INTERIORS.value
    except KeyError as key:
        raise KeyError('In the process of adjusting wall objects, a key error occured') from key
    except Exception as e:
        print(f'an error has occured: {e}')
    return df

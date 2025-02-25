# pylint: disable=C0103, W0718
"""Defines One Click and Tally Filter classes to update values in CLF Omni Column"""
from typing import Dict
import pandas as pd
from wblca_benchmark_v2_data_prep.lca_results.abstract_filters \
    import AbstractFilter
from wblca_benchmark_v2_data_prep.lca_results.enums import OmniClassLevelOne


class RefinedElementFilter(AbstractFilter):
    """Methods to update CLF Omni column for refined element mapping."""
    def filtering(self, df: pd.DataFrame,
                  all_filters: Dict[str, pd.Series]) -> pd.DataFrame:
        df.loc[
            all_filters.get('acous_ceilings_mq_one'),
            self.column_name_to_change
        ] = OmniClassLevelOne.INTERIOR_FINISHES.value
        df.loc[
            all_filters.get('vapor_barrier_mq_one'),
            self.column_name_to_change
        ] = OmniClassLevelOne.ENCLOSURE.value
        df.loc[
            all_filters.get('cladding_mq_one'),
            self.column_name_to_change
        ] = OmniClassLevelOne.ENCLOSURE.value
        df.loc[
            all_filters.get('floor_tile_mq_one'),
            self.column_name_to_change
        ] = OmniClassLevelOne.INTERIOR_FINISHES.value
        df.loc[
            all_filters.get('raised_access_mq_two'),
            self.column_name_to_change
        ] = OmniClassLevelOne.INTERIOR_CONSTRUCTION.value
        df.loc[
            all_filters.get('insulation_mq_one'),
            self.column_name_to_change
        ] = OmniClassLevelOne.ENCLOSURE.value
        self.or_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            or_filters=[
                all_filters.get('clt_mq_two'),
                all_filters.get('glt_mq_two'),
                all_filters.get('wood_i_joist_mq_two'),
                all_filters.get('heavy_timber_mq_two'),
            ]
        )
        self.or_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            or_filters=[
                all_filters.get('hot_rolled_mq_two'),
                all_filters.get('deck_mq_two'),
                all_filters.get('wood_i_joist_mq_two'),
                all_filters.get('heavy_timber_mq_two'),
            ]
        )
        df.loc[
            all_filters.get('ready_mix_lw_mq_two'),
            self.column_name_to_change
        ] = OmniClassLevelOne.SUPERSTRUCTURE.value
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get('unknown_cat_ele_one'),
            ],
            or_filters=[
                all_filters.get('conc_mq_one'),
                all_filters.get('masonry_mq_one'),
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_FINISHES.value,
            and_filters=[
                all_filters.get('unknown_cat_ele_one'),
                all_filters.get('gypsum_board_mq_two'),
            ],
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get('unknown_cat_ele_one'),
            ],
            or_filters=[
                all_filters.get('door_mq_one'),
                all_filters.get('glazing_mq_one'),
                all_filters.get('roofing_mq_one'),
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get('door_mq_one'),
            ],
            or_filters=[
                all_filters.get('superstructure_cat_ele_one'),
                all_filters.get('finishes_cat_ele_one'),
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_CONSTRUCTION.value,
            and_filters=[
                all_filters.get('wood_door_mq_two'),
            ],
            or_filters=[
                all_filters.get('superstructure_cat_ele_one'),
                all_filters.get('finishes_cat_ele_one'),
            ]
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_CONSTRUCTION.value,
            and_filters=[
                all_filters.get('wood_door_frame_mq_two'),
            ],
            or_filters=[
                all_filters.get('superstructure_cat_ele_one'),
                all_filters.get('finishes_cat_ele_one'),
            ]
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get('windows_mq_one'),
                all_filters.get('superstructure_cat_ele_one'),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get('glazing_mq_one'),
                all_filters.get('superstructure_cat_ele_one'),
            ],
        )
        return df

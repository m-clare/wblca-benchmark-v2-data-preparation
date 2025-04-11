# pylint: disable=C0103, W0718
"""Defines One Click Filter classes to update values in CLF Omni Column"""

from typing import Dict
import pandas as pd
from wblca_benchmark_v2_data_prep.lca_results.abstract_filters import AbstractFilter
from wblca_benchmark_v2_data_prep.lca_results.enums import OmniClassLevelOne


class CSIDivision(AbstractFilter):
    """Methods to update CLF Omni column for specific csi division classifications."""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.FFE.value,
            and_filters=[all_filters.get("oc_csi_twelve")],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.FFE.value,
            and_filters=[
                all_filters.get("oc_csi_twenty_five"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.SITEWORK.value,
            and_filters=[
                all_filters.get("oc_csi_thirty_one"),
            ],
        )
        return df


class OmniClassSubstructure(AbstractFilter):
    """Methods to update CLF Omni column for Substructure entries"""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.UNKNOWN.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_sub"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.SUBSTRUCTURE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_sub"),
                all_filters.get("oc_q_fdn"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_sub"),
                all_filters.get("oc_q_vert"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.UNKNOWN.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_sub"),
                all_filters.get("oc_q_horz"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.SUBSTRUCTURE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_sub"),
                all_filters.get("oc_q_horz"),
            ],
            or_filters=[
                all_filters.get("oc_csi_three"),
                all_filters.get("oc_csi_five"),
                all_filters.get("oc_csi_thirty_one"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.SUBSTRUCTURE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_sub"),
                all_filters.get("oc_q_ext"),
            ],
        )
        return df


class OmniClassShellSuperstructure(AbstractFilter):
    """Methods to update CLF Omni column for Shell Superstructure entries"""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.UNKNOWN.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_shell_super"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_shell_super"),
                all_filters.get("oc_q_vert"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_shell_super"),
                all_filters.get("oc_q_horz"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_shell_super"),
                all_filters.get("oc_q_horz"),
            ],
            or_filters=[
                all_filters.get("oc_csi_seven"),
                all_filters.get("oc_csi_eight"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_FINISHES.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_shell_super"),
                all_filters.get("oc_q_horz"),
                all_filters.get("oc_csi_nine"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_shell_super"),
                all_filters.get("oc_q_horz"),
                all_filters.get("oc_csi_nine"),
                all_filters.get("oc_n_glass_sheath"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.UNKNOWN.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_shell_super"),
                all_filters.get("oc_q_other"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_FINISHES.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_shell_super"),
                all_filters.get("oc_q_other"),
                all_filters.get("oc_csi_nine"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_shell_super"),
                all_filters.get("oc_q_other"),
            ],
            or_filters=[
                all_filters.get("oc_csi_seven"),
                all_filters.get("oc_csi_eight"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_shell_super"),
                all_filters.get("oc_q_other"),
            ],
            or_filters=[
                all_filters.get("oc_csi_three"),
                all_filters.get("oc_csi_five"),
                all_filters.get("oc_csi_six"),
                all_filters.get("oc_csi_thirty_one"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_FINISHES.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_shell_super"),
                all_filters.get("oc_q_other"),
            ],
            or_filters=[
                all_filters.get("oc_n_flooring"),
                all_filters.get("oc_n_ceil_pan"),
                all_filters.get("oc_n_acoustic"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_shell_super"),
                all_filters.get("oc_q_other"),
            ],
            or_filters=[
                all_filters.get("oc_n_cladding"),
                all_filters.get("oc_n_glass_sheath"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_shell_super"),
                all_filters.get("oc_q_fdn"),
            ],
        )
        return df


class OmniClassShellEnclosure(AbstractFilter):
    """Methods to update CLF Omni column for Shell Exterior Enclosure entries"""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.UNKNOWN.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_shell_enc"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_shell_enc"),
                all_filters.get("oc_q_vert"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_shell_enc"),
                all_filters.get("oc_q_ext"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_shell_enc"),
                all_filters.get("oc_q_horz"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_shell_enc"),
                all_filters.get("oc_q_horz"),
                all_filters.get("oc_csi_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_shell_enc"),
                all_filters.get("oc_q_horz"),
                all_filters.get("oc_csi_five"),
                all_filters.get("oc_n_deck"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.SUBSTRUCTURE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_shell_enc"),
                all_filters.get("oc_q_fdn"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_CONSTRUCTION.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_shell_enc"),
                all_filters.get("oc_q_int"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_shell_enc"),
                all_filters.get("oc_q_other"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_shell_enc"),
                all_filters.get("oc_q_win_door"),
            ],
        )
        return df


class OmniClassInteriorConstruction(AbstractFilter):
    """Methods to update CLF Omni column for Interior Construction entries"""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_CONSTRUCTION.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_int_con"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.UNKNOWN.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_int_con"),
                all_filters.get("oc_csi_three"),
            ],
        )
        return df


class OmniClassInteriorFinishes(AbstractFilter):
    """Methods to update CLF Omni column for Interior Finishes entries"""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_FINISHES.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_int_fin"),
            ],
        )
        return df


class OmniClassMEP(AbstractFilter):
    """Methods to update CLF Omni column for MEP entries"""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.MEP.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_mep"),
            ],
        )
        return df


class OmniClassNotDefined(AbstractFilter):
    """Methods to update CLF Omni column for undefined OmniClass values"""

    def filtering(
        self, df: pd.DataFrame, all_filters: Dict[str, pd.Series]
    ) -> pd.DataFrame:
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.UNKNOWN.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_nd"),
                all_filters.get("oc_csi_eight"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.UNKNOWN.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_nd"),
                all_filters.get("oc_csi_six"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.UNKNOWN.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_nd"),
                all_filters.get("oc_csi_four"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.FFE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_nd"),
                all_filters.get("oc_csi_ten"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_FINISHES.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_nd"),
                all_filters.get("oc_csi_nine"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_nd"),
                all_filters.get("oc_csi_seven"),
            ],
        )
        self.and_or_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_FINISHES.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_nd"),
                all_filters.get("oc_csi_six"),
            ],
            or_filters=[
                all_filters.get("oc_n_flooring"),
                all_filters.get("oc_n_carpet"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_nd"),
                all_filters.get("oc_csi_six"),
                all_filters.get("oc_n_timber"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.INTERIOR_FINISHES.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_nd"),
                all_filters.get("oc_csi_six"),
                all_filters.get("oc_n_flooring"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_nd"),
                all_filters.get("oc_csi_six"),
                all_filters.get("oc_n_timber"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_nd"),
                all_filters.get("oc_csi_five"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.ENCLOSURE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_nd"),
                all_filters.get("oc_csi_five"),
                all_filters.get("oc_n_cladding"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.SUPERSTRUCTURE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_nd"),
                all_filters.get("oc_csi_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.FFE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_nd"),
                all_filters.get("oc_csi_twelve"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.MEP.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_nd"),
                all_filters.get("oc_csi_twenty_two"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.MEP.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_nd"),
                all_filters.get("oc_csi_twenty_three"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.FFE.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_nd"),
                all_filters.get("oc_csi_twenty_five"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.MEP.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_nd"),
                all_filters.get("oc_csi_twenty_six"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.SITEWORK.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_nd"),
                all_filters.get("oc_csi_thirty_one"),
            ],
        )
        self.and_loc(
            df=df,
            result=OmniClassLevelOne.MEP.value,
            and_filters=[
                all_filters.get("oc_clf_omni_na"),
                all_filters.get("oc_omni_nd"),
                all_filters.get("oc_csi_thirty_three"),
            ],
        )
        # self.and_loc(
        #     df=df,
        #     result=OmniClassLevelOne.UNKNOWN.value,
        #     and_filters=[
        #         all_filters.get('oc_clf_omni_na'),
        #         all_filters.get('oc_omni_nd')
        #     ]
        # )
        return df

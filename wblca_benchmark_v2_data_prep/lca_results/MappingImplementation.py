# pylint: disable=C0103, W0718
"""Implements mapping using mapping elements and materials."""
from abc import abstractmethod
from pathlib import Path
from dataclasses import dataclass, field
from logging import getLogger
import pandas as pd
from wblca_benchmark_v2_data_prep.lca_results.abstract_filters import AbstractFilter
import wblca_benchmark_v2_data_prep.lca_results.all_ele_filters as ele
import wblca_benchmark_v2_data_prep.lca_results.all_mat_filters as mat
import wblca_benchmark_v2_data_prep.lca_results.refined_mat_filters as ref


@dataclass
class Mapper():
    """Interface of mapping.

    Attributes:
        df (pd.DataFrame): DataFrame of raw WBLCA entries
        _filter_type(AbstractFilter): Filter class
        _all_info (dict): Dictionary of all possible filters for raw WBLCA entries
    """
    df: pd.DataFrame = field(repr=False)
    _filter_type: AbstractFilter = None
    _all_info: dict = field(default_factory=dict, repr=False)

    @abstractmethod
    def __post_init__(self):
        self.logger = getLogger(self.__class__.__name__)

    def change_filter_type(self, filter_type: AbstractFilter) -> None:
        """Set filter class.

        Args:
            filter_type (AbstractFilter): Filter class
        """
        self._filter_type = filter_type

    def do_filtering(self) -> None:
        """Update DataFrame using filtering method in filter class"""
        self.logger.info(
            'Filtering using the following class: %s', self._filter_type.__class__.__name__
        )
        self.df = self._filter_type.filtering(self.df, self._all_info)

    def write_csv(self, write_csv_path: Path):
        """Write csv of DataFrame of raw WBLCA entries.

        Raises:
            PermissionError: If file is open, tells user to close the file
        """
        try:
            self.df.to_csv(write_csv_path, index=False)
        except PermissionError as pe:
            self.logger.exception('Permission Error probably caused by having file open')
            raise PermissionError('Try closing the file you are trying to write to') from pe
        self.logger.info('Data has been saved to %s', write_csv_path)

    def write_pickle(self, write_pickle_path: Path):
        """Write pickle of DataFrame of raw WBLCA entries.

        Raises:
            PermissionError: If file is open, tells user to close the file
        """
        try:
            self.df.to_pickle(write_pickle_path)
        except PermissionError as io:
            raise PermissionError('Try closing the file you are trying to write into') from io
        return self


class TallyElementMapper(Mapper):
    """Tally specific element mapper loaded with tally filters"""
    def __post_init__(self):
        super().__post_init__()
        self._all_info = ele.create_all_tally_filters(self.df)
        self.logger.info('%s class created for mapping.', self.__class__.__name__)


class OneClickElementMapper(Mapper):
    """One Click specific element mapper loaded with one click filters"""
    def __post_init__(self):
        super().__post_init__()
        self._all_info = ele.create_all_oneclick_filters(self.df)
        self.logger.info('%s class created for mapping.', self.__class__.__name__)


class TallyMaterialQuantityMapper(Mapper):
    """Tally specific element mapper loaded with tally filters"""
    def __post_init__(self):
        super().__post_init__()
        self._all_info = mat.create_all_tally_filters(self.df)
        self.logger.info('%s class created for mapping.', self.__class__.__name__)


class OneClickMaterialQuantityMapper(Mapper):
    """One Click specific element mapper loaded with one click filters"""
    def __post_init__(self):
        super().__post_init__()
        self._all_info = mat.create_all_oneclick_filters(self.df)
        self.logger.info('%s class created for mapping.', self.__class__.__name__)


class TallyRefinedElementMapper(Mapper):
    """Tally specific element mapper loaded with refined element filters"""
    def __post_init__(self):
        super().__post_init__()
        self._all_info = ref.create_all_refined_filters(self.df)
        self.logger.info('%s class created for mapping.', self.__class__.__name__)


class OneClickRefinedElementMapper(Mapper):
    """One Click specific element mapper loaded with refined element filters"""
    def __post_init__(self):
        super().__post_init__()
        self._all_info = ref.create_all_refined_filters(self.df)
        self.logger.info('%s class created for mapping.', self.__class__.__name__)

from abc import ABC, abstractmethod
from typing import Dict, List
from functools import reduce
import pandas as pd


class AbstractFilter(ABC):
    """Abstract class to update CLF Omni column"""

    def __init__(self, column_name_to_change: str):
        self._column_name_to_change = column_name_to_change

    @property
    def column_name_to_change(self):
        '''abstract method for column name to change in filter'''
        return self._column_name_to_change

    @abstractmethod
    def filtering(self, df: pd.DataFrame,
                  all_filters: Dict[str, pd.Series]) -> None:
        """abstract method to add values to CLF Omni based on provided all_filters

        Args:
            df (pd.DataFrame): DataFrame of One Click entries
            all_filters (Dict[str, pd.Series]): All filters for One Click entries
        """

    def and_loc(self, df: pd.DataFrame, result: str, and_filters: List[pd.Series]) -> None:
        """Wrapper for pandas loc function to include multiple criteria combined with & operator

        Args:
            df (pd.DataFrame): DataFrame of One Click entries
            result (str): Value to be applied to CLF Omni column
            and_filters (List[pd.Series]): Filters applied for loc function

        Raises:
            ValueError: Review one of the and_filter values
        """
        for fil in and_filters:
            if fil is None:
                raise KeyError('One of the and_filters was not entered correctly')

        and_filters_reduced = reduce(
            lambda series_one, series_two: series_one & series_two, and_filters)
        # change columns to object if the column type is float
        if df[self.column_name_to_change].dtype == 'float64':
            df[self.column_name_to_change] = df[self.column_name_to_change].astype(object)
        df.loc[and_filters_reduced, self.column_name_to_change] = result

    def or_loc(self, df: pd.DataFrame, result: str, or_filters: List[pd.Series]) -> None:
        """Wrapper for pandas loc function to include multiple criteria combined with | operator

        Args:
            df (pd.DataFrame): DataFrame of One Click entries
            result (str): Value to be applied to CLF Omni column
            or_filters (List[pd.Series]): Filters applied for loc function

        Raises:
            KeyError: Review one of the or_filter values
        """
        for fil in or_filters:
            if fil is None:
                raise KeyError('One of the or_filters was not entered correctly')

        or_filters_reduced = reduce(
            lambda series_one, series_two: series_one | series_two, or_filters)

        df.loc[or_filters_reduced, self.column_name_to_change] = result

    def and_or_loc(self, df: pd.DataFrame, result: str, and_filters: List[pd.Series],
                   or_filters: List[pd.Series]) -> None:
        """Wrapper for pandas loc function to include multiple criteria.

        Takes filters combined with & operator and filters combined with | operator and
        combines them using & operator.

        Args:
            df (pd.DataFrame): DataFrame of One Click entries
            result (str): Value to be applied to CLF Omni column
            and_filters (List[pd.Series]): Filters to be combined with & operator
            or_filters (List[pd.Series]): Filters to be combined with | operator

        Raises:
            KeyError: Review one of the and_filter or or_filter values
        """
        for fil in and_filters:
            if fil is None:
                raise KeyError('One of the and_filters was not entered correctly')

        for fil in or_filters:
            if fil is None:
                raise KeyError('One of the or_filters was not entered correctly')

        and_filters_reduced = reduce(
            lambda series_one, series_two: series_one & series_two, and_filters)

        or_filters_reduced = reduce(
            lambda series_one, series_two: series_one | series_two, or_filters)

        and_or_filters = and_filters_reduced & or_filters_reduced

        df.loc[and_or_filters, self.column_name_to_change] = result

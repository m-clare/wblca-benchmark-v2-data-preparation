"""Utility functions for src.data.merge."""

from pathlib import Path
from logging import getLogger
import pandas as pd
from wblca_benchmark_v2_data_prep.metadata.general import read_csv
# pylint: disable=W0703

merge_logger = getLogger("metadata.merge")


def read_energy_csv(file_path: Path) -> pd.DataFrame:
    """Read cleaned energy tab csv files.

    Args:
        file_path (Path): file path of cleaned energy csv

    Returns:
        pd.DataFrame: DataFrame of cleaned energy csv or None if error occurs
    """
    merge_logger.info("Reading %s for cleaning", file_path.stem)
    df = read_csv(file_path)
    try:
        df = df.drop(columns=["CLF Proj ID", "CLF Firm ID"])
    except IndexError as ie:
        merge_logger.exception("Could not find column in DataFrame")
        raise IndexError("Could not find column in DataFrame") from ie

    merge_logger.info("Read %s and removed project and firm ids", file_path.stem)
    return df

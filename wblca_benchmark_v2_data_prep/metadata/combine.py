"""Utility functions for src.data.combine."""
from pathlib import Path
from logging import getLogger
import pandas as pd
# pylint: disable=W0703, W0719

combine_logger = getLogger('metadata.combine')


def read_merged_csv(file_path: Path, parse_dates: list) -> pd.DataFrame:
    """Read merged csv files.

    Args:
        file_path (Path): file path of merged csv
        parse_dates (list): columns that should be read as datetime

    Raises:
        PermissionError: Raised if function does not have permission to access file
        IOError: Raised if file cannot be read
        Exception: General exception just in case

    Returns:
        pd.DataFrame: DataFrame of read merged csv
    """
    try:
        combine_logger.info('Reading %s for combining', file_path.stem)
        df = pd.read_csv(
            file_path,
            parse_dates=parse_dates,
            date_format='%Y-%m-%d'
        )
    except PermissionError as pe:
        combine_logger.exception('Permission Error probably caused by having file open')
        raise PermissionError('Try closing out the merged csv file you are trying to read') from pe
    except IOError as io:
        combine_logger.exception('IO Error for csv file')
        raise IOError("Trouble reading merged csv file") from io
    except Exception as e:
        combine_logger.exception('Unknown error has occurred.')
        raise Exception("An unknown error has occured") from e

    df = df.set_index(
        'CLF Model ID'
    )

    df.attrs = {
        'name': df['CLF Firm ID'].unique()[0]
    }
    combine_logger.info('Read merged data from file %s', file_path.name)
    return df

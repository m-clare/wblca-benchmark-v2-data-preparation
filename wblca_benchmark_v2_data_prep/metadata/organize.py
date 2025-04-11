"""Utility functions of src.data.organize."""

from pathlib import Path
import logging
import pandas as pd
# pylint: disable=W0703, W0719

organize_logger = logging.getLogger("metadata.organize")


def read_excel(file_path: Path, sheet_name: str) -> pd.DataFrame:
    """Read raw Data Entry Templates excel files.

    Args:
        file_path (Path): file path of raw data entry template
        sheet_name (str): Excel sheet name to read

    Raises:
        PermissionError: Raised if function does not have permission to access file
        IOError: Raised if file cannot be read
        Exception: General exception just in case

    Returns:
        pd.DataFrame: DataFrame of Excel sheet
    """
    try:
        organize_logger.info("reading %s", file_path.stem)
        df = pd.read_excel(file_path, sheet_name=sheet_name)
    except PermissionError as pe:
        organize_logger.exception(
            "Permission Error probably caused by having file open"
        )
        raise PermissionError("Try closing out the file you are trying to read") from pe
    except IOError as io:
        organize_logger.exception("IO Error for csv file")
        raise IOError("Trouble reading excel file") from io
    except Exception as e:
        organize_logger.exception("Unknown error has occurred.")
        raise Exception("An unknown error has occured") from e
    organize_logger.info(
        "Read data from sheet %s from file %s", sheet_name, file_path.name
    )
    try:
        df.attrs = {
            # hard coded value of the firm name
            "name": df.iloc[0, 3]
        }
    except IndexError:
        organize_logger.warning(
            "Also, Encountered an indexing error, used first two letters of file name"
        )
        df.insert(3, file_path.stem[0:2], "")
        df.iloc[0, 3] = file_path.stem[0:2]
        df.attrs = {
            # hard coded value of the firm name
            "name": df.iloc[0, 3]
        }

    return df


def replace_columns(
    df: pd.DataFrame, replacements_yaml: dict, replacement_list_name: str
) -> pd.DataFrame:
    """Replace column names for the raw data entry template.

    Args:
        df (pd.DataFrame): raw data entry template
        replacements_yaml (dict): dictionary from yaml file
        replacement_list_name (str): name of key for dictionary of column name

    Returns:
        pd.DataFrame: data entry template with column names replaced, if applicable
    """
    organize_logger.info("Begin replacing columns based on replacement_list_name.")
    if replacements_yaml.get(replacement_list_name):
        df["Field"] = df["Field"].replace(replacements_yaml.get(replacement_list_name))
        organize_logger.info("Replaced column values!")
        return df

    organize_logger.warning("No changes made to data entry template based on yaml")
    return df


def column_name_test(df: pd.DataFrame, original_col_list: list) -> None:
    """Test the original column list before transposing.

    Tests against the data entry template's columns using pd.testing.assert_series_equal.

    Args:
        df (pd.DataFrame): DataFrame with raw data entry template
        original_col_list (list): original column list from yaml
    """
    test_series = pd.Series(original_col_list)
    try:
        pd.testing.assert_series_equal(test_series, df.Field, check_names=False)
    except AssertionError as e:
        for error in str(e).split("\n")[6:]:
            organize_logger.error(
                "Column name issue for firm %s: %s", df.iloc[0, 3], error
            )

    organize_logger.info("There were no issues with column names")


def transpose_data(df: pd.DataFrame, columns_to_drop: list) -> pd.DataFrame:
    """Transposes raw data entry template into a DataFrame.

    Performs the following:
    - drops columns based on columns_to_drop input
    - transposes the DataFrame
    - resets the index
    - drops the index column
    - renames the columns based on the Field variable
    - removes the duplicate row with column names
    - set the index as 'CLF Model ID' for identification purposes

    Args:
        df (pd.DataFrame): Unedited data entry template
        col_to_drop (dict): columns to drop based on sheet

    Returns:
        pd.DataFrame: cleaned DataFrame
    """
    try:
        organize_logger.info("Begin transposing data.")
        df1 = (
            df.drop(columns=columns_to_drop)
            .transpose()
            .reset_index()
            .drop(columns="index")
            .rename(columns=df.iloc[:, 2].to_dict())
            .drop(0)
            .set_index("CLF Model ID")
        )
    except IndexError as ie:
        organize_logger.exception("Could not find column index in DataFrame")
        raise IndexError('Could not find column "index" in DataFrame') from ie
    except Exception as e:
        organize_logger.exception("unknown error has occured")
        raise Exception("An unknown error has occured") from e
    organize_logger.info("Transposed data for firm %s", df.attrs.get("name"))
    return df1


def column_name_after_transpose_test(df: pd.DataFrame, original_col_list: list) -> None:
    """
    Test the original column list after transposing.

    Tests against the data entry template's columns using Index.difference.

    Args:
        df (pd.DataFrame): DataFrame with transposed data entry template
        original_col_list (list): original column list from yaml
    """
    test_index = pd.Index(original_col_list)
    index_difference = test_index.difference(df.reset_index().columns).to_list()
    organize_logger.info("Begin column name test after transposition.")
    if len(index_difference) == 0:
        organize_logger.info(
            "There were no issues with column names after \
transpose for firm %s",
            df.attrs.get("name"),
        )
    for column in index_difference:
        organize_logger.error(
            "Column Name issue after transpose for firm %s: %s",
            df.attrs.get("name"),
            column,
        )

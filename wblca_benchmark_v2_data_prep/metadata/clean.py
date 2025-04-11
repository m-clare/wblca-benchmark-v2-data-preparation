"""Utility function for src.data.clean."""

from logging import getLogger
import pandas as pd
# pylint: disable=W0703, W0719

clean_logger = getLogger("metadata.clean")


def dropdown_replace(
    df: pd.DataFrame, dropdown_cols: dict, dropdown_replacements: dict
) -> pd.DataFrame:
    """Replace dropdown column values based on yaml input.

    Args:
        df (pd.DataFrame): DataFrame with organized data entry template
        dropdown_cols (dict): dictionary that correlates column dropdown type
        with column name in the DataFrame
        dropdown_replacements (dict): dictionary with replacement information
        per dropdown column

    Returns:
        pd.DataFrame: DataFrame with replaced values in dropdown columns
    """
    for key, col_list in dropdown_cols.items():
        for col in col_list:
            try:
                clean_logger.info(
                    "Trying to replace dropdown values for column %s.", col
                )
                if dropdown_replacements.get(key):
                    df[col] = df[col].replace(dropdown_replacements.get(key))
            except ValueError as ve:
                clean_logger.exception(
                    "Could not find dictionary %s", dropdown_replacements
                )
                raise ValueError(
                    f"Could not find dictionary {dropdown_replacements}"
                ) from ve
            except IndexError as ie:
                clean_logger.exception("Could not find column %s in DataFrame", col)
                raise IndexError(f"Could not find column {col} in DataFrame") from ie
            except Exception as e:
                clean_logger.exception("Unknown error has occurred")
                raise Exception("An unknown error has occured") from e
    clean_logger.info("All dropdown values replaced for firm %s", df.attrs.get("name"))
    return df


def data_type_replace(
    df: pd.DataFrame,
    string_list: list,
    int_list: list,
    float_list: list,
    datetime_list: list,
) -> pd.DataFrame:
    """Replace data type values based on yaml output.

    Args:
        df (pd.DataFrame): DataFrame with organized data entry template
        string_list (list): list of columns with string data type
        int_list (list): list of columns with int data type
        float_list (list): list of columns with float data type
        date_list (list): list of columns with date data type

    Returns:
        pd.DataFrame: DataFrame with replaced values by data type
    """
    df = df.reset_index()
    # run string test
    clean_logger.info("Begin replacing all data types.")
    updated_df = (
        df.pipe(string_type_replace, string_list)
        .pipe(int_type_replace, int_list)
        .pipe(float_type_replace, float_list)
        .pipe(datetime_type_replace, datetime_list)
    )

    updated_df = updated_df.set_index("CLF Model ID")
    clean_logger.info("All data types replaced for firm %s,", df.attrs.get("name"))
    return updated_df


def string_type_replace(df: pd.DataFrame, string_list: list) -> pd.DataFrame:
    """Replace type of column to string.

    Args:
        df (pd.DataFrame): DataFrame to be adjusted
        string_list (list): list of columns in DataFrame to become strings

    Raises:
        ValueError: Raised if column cannot be cast to string
        IndexError: Raised if column name cannot be found in DataFrame
        Exception: Raised if an unknown error occurs

    Returns:
        pd.DataFrame: DataFrame with selected column types adjusted to strings
    """
    for string_col in string_list:
        try:
            clean_logger.info("Begin replacing string types for column %s.", string_col)
            df[string_col] = df[string_col].astype("string")
        except ValueError as ve:
            clean_logger.exception("Could not cast to string at column %s", string_col)
            raise ValueError(f"Could not cast to string at column {string_col}") from ve
        except IndexError as ie:
            clean_logger.exception("Could not find column %s in DataFrame", string_col)
            raise IndexError(f"Could not find column {string_col} in DataFrame") from ie
        except Exception as e:
            clean_logger.exception("Unknown error has occurred")
            raise Exception("An unknown error has occured") from e
        clean_logger.info("Replaced string types.")
    return df


def int_type_replace(df: pd.DataFrame, int_list: list) -> pd.DataFrame:
    """Replace type of column to int.

    Args:
        df (pd.DataFrame): DataFrame to be adjusted
        int_list (list): list of columns in DataFrame to become ints

    Raises:
        ValueError: Raised if column cannot be cast to int
        IndexError: Raised if column name cannot be found in DataFrame
        Exception: Raised if an unknown error occurs

    Returns:
        pd.DataFrame: DataFrame with selected column types adjusted to ints
    """
    for int_col in int_list:
        try:
            clean_logger.info("Begin replacing int types for column %s.", int_col)
            df[int_col] = pd.to_numeric(
                df[int_col], downcast="integer", errors="coerce"
            )
        except ValueError as ve:
            clean_logger.exception("Could not cast to int at column %s", int_col)
            raise ValueError(f"Could not cast to int at column {int_col}") from ve
        except IndexError as ie:
            clean_logger.exception("Could not find column %s in DataFrame", int_col)
            raise IndexError(f"Could not find column {int_col} in DataFrame") from ie
        except Exception as e:
            clean_logger.exception("Unknown error has occurred")
            raise Exception("An unknown error has occured") from e
        clean_logger.info("Replaced int types.")
    return df


def float_type_replace(df: pd.DataFrame, float_list: list) -> pd.DataFrame:
    """Replace type of column to float.

    Args:
        df (pd.DataFrame): DataFrame to be adjusted
        float_list (list): list of columns in DataFrame to become floats

    Raises:
        ValueError: Raised if column cannot be cast to float
        IndexError: Raised if column name cannot be found in DataFrame
        Exception: Raised if an unknown error occurs

    Returns:
        pd.DataFrame: DataFrame with selected column types adjusted to floats
    """
    for float_col in float_list:
        try:
            clean_logger.info("Begin replacing float types for column %s.", float_col)
            df[float_col] = pd.to_numeric(df[float_col], errors="coerce")
        except ValueError as ve:
            clean_logger.exception("Could not cast to float at column %s", float_col)
            raise ValueError(f"Could not cast to float at column {float_col}") from ve
        except IndexError as ie:
            clean_logger.exception("Could not find column %s in DataFrame", float_col)
            raise IndexError(f"Could not find column {float_col} in DataFrame") from ie
        except Exception as e:
            clean_logger.exception("Unknown error has occurred")
            raise Exception("An unknown error has occured") from e
        clean_logger.info("Replaced float types.")
    return df


def datetime_type_replace(df: pd.DataFrame, datetime_list: list) -> pd.DataFrame:
    """Replace type of column to datetime.

    Args:
        df (pd.DataFrame): DataFrame to be adjusted
        datetime_list (list): list of columns in DataFrame to become datetime

    Raises:
        ValueError: Raised if column cannot be cast to float
        IndexError: Raised if column name cannot be found in DataFrame
        Exception: Raised if an unknown error occurs

    Returns:
        pd.DataFrame: DataFrame with selected column types adjusted to datetime
    """
    for datetime_col in datetime_list:
        try:
            clean_logger.info(
                "Begin replacing datetime types for column %s.", datetime_col
            )
            df[datetime_col] = pd.to_datetime(
                df[datetime_col], format="mixed", errors="coerce", yearfirst=True
            )
        except ValueError as ve:
            clean_logger.exception(
                "Could not cast to datetime at column %s", datetime_col
            )
            raise ValueError(
                f"Could not cast to datetime at column {datetime_col}"
            ) from ve
        except IndexError as ie:
            clean_logger.exception(
                "Could not find column %s in DataFrame", datetime_col
            )
            raise IndexError(
                f"Could not find column {datetime_col} in DataFrame"
            ) from ie
        except Exception as e:
            clean_logger.exception("Unknown error has occurred")
            raise Exception("An unknown error has occured") from e
        clean_logger.info("Replaced datetime types.")
    return df

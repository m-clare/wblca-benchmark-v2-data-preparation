"""Utility functions for general use in the project workflow."""

from pathlib import Path
import logging
import pandas as pd
import yaml
# pylint: disable=W0703, W0719

general_logger = logging.getLogger("metadata.general")


def read_csv(file_path: Path) -> pd.DataFrame:
    """Read csv files for general use.

    Args:
        file_path (Path): file path of csv to read

    Raises:
        PermissionError: Raised if function does not have permission to access file
        IOError: Raised if file cannot be read
        Exception: General exception just in case

    Returns:
        pd.DataFrame: DataFrame of read csv file
    """
    try:
        general_logger.info("Reading %s", file_path.stem)
        df = pd.read_csv(
            file_path,
        )
    except PermissionError as pe:
        general_logger.exception("Permission Error probably caused by having file open")
        raise PermissionError("Try closing out the file you are trying to read") from pe
    except IOError as io:
        general_logger.exception("IO Error for csv file")
        raise IOError("Trouble reading csv file") from io
    except Exception as e:
        general_logger.exception("Unknown error has occurred.")
        raise Exception("An unknown error has occured") from e

    df = df.set_index("CLF Model ID")

    df.attrs = {"name": df["CLF Firm ID"].unique()[0]}
    general_logger.info("Read data from file %s", file_path.name)
    return df


def read_yaml(file_path: Path) -> dict:
    """Read yaml files for general use.

    Args:
        file_path (Path): file path of yaml to read

    Raises:
        PermissionError: Raised if function does not have permission to access file
        IOError: Raised if file cannot be read
        Exception: General exception just in case

    Returns:
        dict: dictionary with yaml information or None if error occurs
        str: Logged information in form of Exception or string
    """
    try:
        general_logger.info("reading %s", file_path.stem)
        with open(file=file_path, mode="r", encoding="utf-8") as file:
            yaml_dict = yaml.safe_load(file)
    except PermissionError as pe:
        general_logger.exception("Permission Error probably caused by having file open")
        raise PermissionError("Try closing out the file you are trying to read") from pe
    except IOError as io:
        general_logger.exception("IO Error for csv file")
        raise IOError("Trouble reading yaml file") from io
    except Exception as e:
        general_logger.exception("Unknown error has occurred.")
        raise Exception("An unknown error has occured") from e

    general_logger.info("%s yaml read", file_path.stem)

    return yaml_dict


def write_to_csv(
    df: pd.DataFrame, write_directory: Path, file_suffix: str, module_description: str
) -> str:
    """Write to csv for general use.

    This function allows you to name the file based on the name of the firm as well as a file suffix
    to be appended to the end of the file name.

    Args:
        df (pd.DataFrame): DataFrame to write to csv
        write_directory (Path): Path location to write csv to
        file_suffix (str): Any additional information to append to the end of the file name
        module_description (str): For logging, this outputs where the file has been saved

    Raises:
        PermissionError: Raised if function does not have permission to access file
        IOError: Raised if file cannot be written
        Exception: General exception just in case

    Returns:
        str: logged info of written csv
    """
    try:
        df.to_csv(write_directory.joinpath(f"{df.attrs.get('name')}{file_suffix}"))
    except PermissionError as pe:
        general_logger.exception("Permission Error probably caused by having file open")
        raise PermissionError("Try closing out the file you are trying to read") from pe
    except IOError as io:
        general_logger.exception("IO Error for csv file")
        raise IOError("Trouble writing csv file") from io
    except Exception as e:
        general_logger.exception("Unknown error has occurred.")
        raise Exception("An unknown error has occured") from e

    general_logger.info(
        "data entry template for firm %s has \
been saved in the %s folder",
        df.attrs.get("name"),
        module_description,
    )

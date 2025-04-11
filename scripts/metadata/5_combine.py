# pylint: disable=C0103, R0801, R0914, W0703
"""Combine data entry templates."""

from pathlib import Path
import warnings
from logging import getLogger
import pandas as pd
import pandera as pa
from wblca_benchmark_v2_data_prep.utils.loggers import setup_logger
from wblca_benchmark_v2_data_prep.metadata.det_schema import (
    get_project_det_schema,
    get_energy_det_schema,
)
import wblca_benchmark_v2_data_prep.metadata.general as utils
import wblca_benchmark_v2_data_prep.metadata.combine as co_utils
# pylint: disable=W0703, W0719


def combine_det():
    """
    Combine all merged data entry templates.

    This function does the following:

    - Reads yaml files with key dropdown and data type information
    - Reads merged data entry templates
    - Concatenates all data entry templates into one DataFrame
    - Re-tests dropdown values
    - Writes combined data entry templates to combined directory

    """
    warnings.simplefilter(action="ignore", category=FutureWarning)
    current_file_path = Path(__file__)
    main_directory = current_file_path.parents[2]
    config_path = main_directory.joinpath("references/config_metadata.yml")

    # instantiate logger
    setup_logger(
        log_file_path=main_directory.joinpath("data/logs/metadata/combine_det.log"),
        level="info",
    )

    main_combine_logger = getLogger("5_combine_script")
    main_combine_logger.info("Logger has been set up.")

    main_combine_logger.info("Begin configuration.")
    config = utils.read_yaml(config_path)
    config_dict = config.get(current_file_path.stem)
    assert config_dict is not None, "The config dictionary could not be set"

    # set module level local variables from config
    read_data_directory = config_dict.get("read_data_directory")
    read_data_filter = config_dict.get("read_data_filter")
    col_dtypes_yaml = config_dict.get("col_dtypes")
    write_data_directory = config_dict.get("write_data_directory")
    module_description = config_dict.get("module_description")
    dataframe_name = config_dict.get("dataframe_name")
    file_suffix = config_dict.get("file_suffix")
    schema_column_removal = config_dict.get("schema_column_removal")

    # set paths
    read_data_directory_path = main_directory.joinpath(read_data_directory).glob(
        read_data_filter
    )
    col_dtypes_path = main_directory.joinpath(col_dtypes_yaml)
    write_data_directory_path = main_directory.joinpath(write_data_directory)

    # read yaml
    col_dtypes = utils.read_yaml(col_dtypes_path)
    main_combine_logger.info("End configuration.")

    # read merged dets
    df_list = []
    main_combine_logger.info("Begin reading all merged data entry templates.")
    for file in read_data_directory_path:
        df = co_utils.read_merged_csv(file, col_dtypes.get("parse_dates"))
        df_list.append(df)
    main_combine_logger.info("Read all merged data entry templates.")

    main_combine_logger.info(
        "Begin concatenation process of all merged data entry templates."
    )
    try:
        final_df = pd.concat(df_list)
        final_df.attrs = {"name": dataframe_name}
    except Exception as e:
        main_combine_logger.exception("Issue during concatenation")
        raise Exception("Issue during concatenation") from e
    main_combine_logger.info("All merged data entry templates concatenated!")

    # schema updates
    main_combine_logger.info("Create new schema for combined data entry templates.")
    project_schema = get_project_det_schema()
    energy_schema = get_energy_det_schema().remove_columns(schema_column_removal)
    schema = project_schema.add_columns(energy_schema.columns)

    # validate final det
    try:
        main_combine_logger.info("Validating final combined schema.")
        schema.validate(final_df, lazy=True)
    except pa.errors.SchemaErrors as e:
        for error in e.schema_errors:
            main_combine_logger.warning(error)
    main_combine_logger.info("Validation process complete.")

    # write to csv
    utils.write_to_csv(
        final_df, write_data_directory_path, file_suffix, module_description
    )


if __name__ == "__main__":
    combine_det()

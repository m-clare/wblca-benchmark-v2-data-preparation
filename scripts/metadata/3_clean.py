# pylint: disable=C0103, R0801, R0914, R0915
"""Clean project and energy data entry templates."""

from pathlib import Path
from logging import getLogger
from wblca_benchmark_v2_data_prep.utils.loggers import setup_logger
import wblca_benchmark_v2_data_prep.metadata.clean as cl_utils
import wblca_benchmark_v2_data_prep.metadata.general as utils


def clean_det(project_or_energy: str):
    """
    Clean data entry templates with data from 2_test.

    This function does the following:

    - Reads yaml files with key dropdown and data type information
    - Organize lists based on data type
    - Replaces incorrect dropdown values, where applicable
    - Replaces incorrect data types, where applicable
    - Writes cleaned data entry templates in cleaned directory
    """
    current_file_path = Path(__file__)
    main_directory = current_file_path.parents[2]
    config_path = main_directory.joinpath("references/config_metadata.yml")

    # instantiate logger
    setup_logger(
        log_file_path=main_directory.joinpath(
            f"data/logs/metadata/{project_or_energy}_clean.log"
        ),
        level="info",
    )

    main_clean_logger = getLogger("3_clean_script")
    main_clean_logger.info("Logger has been set up.")

    main_clean_logger.info("Begin configuration.")
    config = utils.read_yaml(config_path)
    config_dict = config.get(current_file_path.stem)
    assert config_dict is not None, "The config dictionary could not be set"

    project_or_energy_flag = config_dict.get(project_or_energy)
    assert project_or_energy_flag is not None, (
        "The config could not set project or energy variable"
    )

    # set module level local variables from config
    dropdown_cols_yaml = config_dict.get("dropdown_cols")
    dropdown_replacements_yaml = config_dict.get("dropdown_replacements")
    col_dtypes_yaml = config_dict.get("col_dtypes")
    read_data_directory = config_dict.get("read_data_directory")
    write_data_directory = config_dict.get("write_data_directory")
    module_description = config_dict.get("module_description")

    # set project or energy level local variables from config
    read_data_filter = project_or_energy_flag.get("read_data_filter")
    data_types = project_or_energy_flag.get("data_types")
    parse_dates = project_or_energy_flag.get("parse_dates")
    cleaned_file_suffix = project_or_energy_flag.get("cleaned_file_suffix")

    # set paths
    read_data_directory_path = main_directory.joinpath(read_data_directory).glob(
        read_data_filter
    )
    dropdown_cols_path = main_directory.joinpath(dropdown_cols_yaml)
    dropdown_replacements_path = main_directory.joinpath(dropdown_replacements_yaml)
    col_dtypes_path = main_directory.joinpath(col_dtypes_yaml)
    write_data_directory_path = main_directory.joinpath(write_data_directory)

    if project_or_energy == "project":
        replace_data = True
    elif project_or_energy == "energy":
        replace_data = False
    else:
        main_clean_logger.warning(
            "project_or_energy can only have the inputs project or energy"
        )
        raise ValueError("project_or_energy can only have the inputs project or energy")

    # read yamls
    dropdown_cols = utils.read_yaml(dropdown_cols_path)

    dropdown_replacements = utils.read_yaml(dropdown_replacements_path)

    col_dtypes = utils.read_yaml(col_dtypes_path)
    assert col_dtypes is not None, "The column dtypes yaml could not be read."

    if replace_data:
        dtype_dict = col_dtypes.get(data_types)
        assert dtype_dict is not None, (
            "The data types of the columns could not be read."
        )
        date_list = col_dtypes.get(parse_dates)
        assert date_list is not None, "The columns with date formats could not be read."
        date_list_checked = list(date_list)

        string_list = [key for (key, value) in dtype_dict.items() if value == "string"]
        int_list = [key for (key, value) in dtype_dict.items() if value == "Int64"]
        float_list = [key for (key, value) in dtype_dict.items() if value == "Float64"]
    main_clean_logger.info("End configuration.")

    for file in read_data_directory_path:
        main_clean_logger.info("Begin cleaning data entry template %s", file.stem)
        df = utils.read_csv(file)
        if replace_data:
            df = cl_utils.dropdown_replace(df, dropdown_cols, dropdown_replacements)

            df = cl_utils.data_type_replace(
                df, string_list, int_list, float_list, date_list_checked
            )
        main_clean_logger.info("End cleaning data entry template %s", file.stem)

        utils.write_to_csv(
            df, write_data_directory_path, cleaned_file_suffix, module_description
        )


if __name__ == "__main__":
    clean_det("project")
    clean_det("energy")

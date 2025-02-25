# pylint: disable=C0103, R0801, R0914
"""Organize project and energy data entry templates."""
from pathlib import Path
from logging import getLogger
from wblca_benchmark_v2_data_prep.utils.loggers import setup_logger
import wblca_benchmark_v2_data_prep.metadata.organize as o_utils
import wblca_benchmark_v2_data_prep.metadata.general as utils


def organize_det(project_or_energy: str):
    """
    Organize project and energy tabs from data entry templates.

    This function does the following:

    - Reads yaml files with column name replacements
    - Reads raw data entry templates
    - Tests column names
    - Replaces column names to ensure they are all correct
    - Transposes data
    - Tests again column names are correct
    - Writes transposed data entry templates to data/organized

    """
    current_file_path = Path(__file__)
    main_directory = current_file_path.parents[2]
    config_path = main_directory.joinpath('references/config_metadata.yml')

    # instantiate logger
    setup_logger(
        log_file_path=main_directory.joinpath(
            f'data/logs/metadata/{project_or_energy}_organize.log'
        ),
        level='info'
    )

    main_organize_logger = getLogger('1_organize_script')
    main_organize_logger.info('Logger has been set up.')

    main_organize_logger.info('Begin configuration.')
    config = utils.read_yaml(config_path)

    config_dict = config.get(current_file_path.stem)
    assert config_dict is not None, 'The config dictionary could not be set'

    project_or_energy_flag = config_dict.get(project_or_energy)
    assert project_or_energy_flag is not None, 'The config could not set project or energy variable'

    # set module level local variables from config
    read_data_directory = config_dict.get('read_data_directory')
    read_data_filter = config_dict.get('read_data_filter')
    write_data_dictectory = config_dict.get('write_data_directory')
    module_description = config_dict.get('module_description')
    col_name_replacements_yaml = config_dict.get('col_name_replacements')

    # set project or energy level local variables from config
    sheet_name = project_or_energy_flag.get('sheet_name')
    original_column_list = project_or_energy_flag.get('original_column_list')
    replacement_list = project_or_energy_flag.get('replacement_list')
    column_list_to_remove = project_or_energy_flag.get('column_list_to_remove')
    organized_file_suffix = project_or_energy_flag.get('organized_file_suffix')

    # set paths
    read_data_directory_path = main_directory.joinpath(
        read_data_directory
    ).glob(read_data_filter)
    write_data_directory_path = main_directory.joinpath(write_data_dictectory)
    col_name_replacements_path = main_directory.joinpath(col_name_replacements_yaml)

    # read yamls
    replacements = utils.read_yaml(col_name_replacements_path)
    original_column_list = replacements.get(original_column_list)
    assert original_column_list is not None, 'The function was not able to read\
the original column list'
    main_organize_logger.info('End configuration.')

    df_list = []
    # loop over each raw data entry template
    for file in read_data_directory_path:
        main_organize_logger.info('Begin organizing data entry template %s', file.stem)
        # read excel tab
        df = o_utils.read_excel(
            file,
            sheet_name,
        )

        # test column names
        o_utils.column_name_test(
            df,
            original_column_list
        )

        # replace column names
        df = o_utils.replace_columns(
            df,
            replacements,
            replacement_list
        )

        # transpose excel sheet
        df1 = o_utils.transpose_data(
            df,
            column_list_to_remove
        )

        # recheck column names
        o_utils.column_name_after_transpose_test(
            df1,
            original_column_list
        )

        df_list.append(df1)
        main_organize_logger.info('End organizing data entry template %s', file.stem)

    # loop over each sheet that was read
    for det_df in df_list:
        # write to csv
        utils.write_to_csv(
            det_df,
            write_data_directory_path,
            organized_file_suffix,
            module_description
        )


if __name__ == "__main__":
    organize_det('project')
    organize_det('energy')

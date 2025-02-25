# pylint: disable=C0103, R0801, R0914
"""Test project and energy data entry templates."""
from pathlib import Path
import warnings
from logging import getLogger
import pandera as pa
from wblca_benchmark_v2_data_prep.utils.loggers import setup_logger
import wblca_benchmark_v2_data_prep.metadata.general as utils
from wblca_benchmark_v2_data_prep.metadata.det_schema import get_project_det_schema, \
    get_energy_det_schema


def test_det(project_or_energy: str):
    """
    This function does the following:

    - Tests values using pandera
    - Outputs key logging information

    """

    warnings.simplefilter(action='ignore', category=FutureWarning)
    current_file_path = Path(__file__)
    main_directory = current_file_path.parents[2]
    config_path = main_directory.joinpath('references/config_metadata.yml')
    # instantiate logger
    setup_logger(
        log_file_path=main_directory.joinpath(
            f'data/logs/metadata/{project_or_energy}_test.log'
        ),
        level='info'
    )
    main_test_logger = getLogger('2_test_script')
    main_test_logger.info('Logger has been set up.')

    main_test_logger.info('Begin configuration.')
    config = utils.read_yaml(config_path)
    config_dict = config.get(current_file_path.stem)
    assert config_dict is not None, 'The config dictionary could not be set'

    project_or_energy_flag = config_dict.get(project_or_energy)
    assert project_or_energy_flag is not None, 'The config could not set project or energy variable'

    # set module level local variables from config
    read_data_directory = config_dict.get('read_data_directory')

    # set project or energy level local variables from config
    read_data_filter = project_or_energy_flag.get('read_data_filter')

    # set paths
    read_data_directory_path = main_directory.joinpath(
        read_data_directory
    ).glob(read_data_filter)
    main_test_logger.info('End configuration.')

    if project_or_energy == "project":
        schema = get_project_det_schema()
    elif project_or_energy == "energy":
        schema = get_energy_det_schema()
    else:
        main_test_logger.error('project_or_energy can only have the inputs project or energy')
        raise ValueError('project_or_energy can only have the inputs project or energy')

    for file in read_data_directory_path:
        # read organized csv
        test_df = utils.read_csv(
            file
        )
        # dropdown testing
        try:
            schema.validate(test_df, lazy=True)
        except pa.errors.SchemaErrors as e:
            for error in e.schema_errors:
                main_test_logger.error(error)
        main_test_logger.info('Finished testing schema for firm %s', test_df.attrs.get('name'))
    return None


if __name__ == '__main__':
    test_det('energy')
    test_det('project')

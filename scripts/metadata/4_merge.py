# pylint: disable=C0103, R0801, R0914
"""Merge project and energy data entry templates."""
from pathlib import Path
from logging import getLogger
import pandas as pd
from wblca_benchmark_v2_data_prep.utils.loggers import setup_logger
import wblca_benchmark_v2_data_prep.metadata.merge as m_utils
import wblca_benchmark_v2_data_prep.metadata.general as utils
# pylint: disable=W0703, W0719


def merge_det():
    """
    Merge project and energy tabs from data entry templates.

    This function does the following:

    - Reads the project and energy dets
    - Finds the project and energy dets of the same project
    - Merges them together
    - Writes merged files to merged directory
    """
    current_file_path = Path(__file__)
    main_directory = current_file_path.parents[2]
    config_path = main_directory.joinpath('references/config_metadata.yml')

    # instantiate logger
    setup_logger(
        log_file_path=main_directory.joinpath(
            'data/logs/metadata/merge_det.log'
        ),
        level='info'
    )

    main_merge_logger = getLogger('1_organize_script')
    main_merge_logger.info('Logger has been set up.')

    main_merge_logger.info('Begin configuration.')
    config = utils.read_yaml(config_path)

    # set module level local variables from config
    read_data_directory = config\
        .get(current_file_path.stem).get('read_data_directory')
    read_data_filter = config\
        .get(current_file_path.stem).get('read_data_filter')
    write_data_directory = config.\
        get(current_file_path.stem).get('write_data_directory')
    module_description = config.\
        get(current_file_path.stem).get('module_description')
    merged_file_suffix = config.\
        get(current_file_path.stem).get('merged_file_suffix')

    # set paths
    read_data_directory_path = main_directory.joinpath(
        read_data_directory
    ).glob(read_data_filter)
    read_data_directory_for_filtering = main_directory.joinpath(
        read_data_directory
    )
    write_data_directory_path = main_directory.joinpath(write_data_directory)
    main_merge_logger.info('End configuration.')

    firm_list = []
    main_merge_logger.info('Collecting firm names.')
    for file in read_data_directory_path:
        df = utils.read_csv(
            file
        )
        firm_list.append(df.attrs.get('name'))
    main_merge_logger.info('Collected firm names.')
    firm_names = pd.Series(firm_list).unique().tolist()

    for firm in firm_names:
        main_merge_logger.info('Merging for firm %s', firm)
        energy_det = list(read_data_directory_for_filtering.glob(f'*{firm}_energy*'))[0]
        project_det = list(read_data_directory_for_filtering.glob(f'*{firm}_project*'))[0]

        e_det_df = m_utils.read_energy_csv(
            energy_det
        )

        p_det_df = utils.read_csv(
            project_det
        )

        try:
            merged_det = p_det_df.join(e_det_df)
            merged_det.attrs = {
                'name': firm
            }
        except Exception as e:
            main_merge_logger.exception('Issue during joining')
            raise Exception("Issue during joining") from e

        main_merge_logger.info('Merged project and energy data entry templates.')
        utils.write_to_csv(
            merged_det,
            write_data_directory_path,
            merged_file_suffix,
            module_description
        )
        main_merge_logger.info('Finished merging for firm %s', firm)


if __name__ == '__main__':
    merge_det()

# pylint: disable=C0103
"""Create public dataset internal data."""

from pathlib import Path
from logging import getLogger
import pandas as pd
import wblca_benchmark_v2_data_prep.utils.general as gen
import wblca_benchmark_v2_data_prep.data_record.internal_data_calcs as calc
from wblca_benchmark_v2_data_prep.utils.loggers import setup_logger


def create_internal_data():
    """
    Creates an internal dataset to aid in the creation of the data record.

    This script does the following:

    - Reads the combined data entry templates.
    - Removes projects that are not in the given design phase or final reports.
    - Reorders and renames columns for data record.
    - Writes internal data to excel.
    """
    main_directory = Path(__file__).parents[2]
    dets_path = main_directory.joinpath(
        "data/data_record/raw/Project_Data_Finalized.csv"
    )
    config_path = main_directory.joinpath("references/config_data_record.yml")
    internal_directory = main_directory.joinpath("data/data_record/internal")

    # instantiate logger
    setup_logger(
        log_file_path=main_directory.joinpath(
            "data/logs/data_record/internal_data.log"
        ),
        level="info",
    )

    internal_data_logger = getLogger("1_internal_data_script")
    internal_data_logger.info("Logger has been set up.")

    internal_data_logger.info("Read data entry templates file.")
    dets = pd.read_csv(dets_path, index_col=False)

    internal_data_logger.info("Begin configuration.")
    config = gen.read_yaml(config_path)
    assert config is not None, "The config dictionary could not be set"

    impact_type_list = config.get("impact_type")
    assert impact_type_list is not None, "The list for impact types could not be set"

    design_phases_list = config.get("design_phases")
    assert design_phases_list is not None, "The list for impact types could not be set"

    column_value_replace = config.get("column_value_replace")
    assert column_value_replace is not None, (
        "The list for cols to replace could not be set"
    )

    public_dataset_column_renaming = config.get("public_dataset_column_renaming")
    assert public_dataset_column_renaming is not None, (
        "The dict for col renaming could not be set"
    )

    internal_data_col_order = config.get("internal_data_col_order")
    assert internal_data_col_order is not None, (
        "The list for metadata col order could not be set"
    )
    internal_data_logger.info("End configuration.")

    internal_data_logger.info("Begin internal data creation.")
    internal_data = calc.create_internal_data(
        accepted_design_phases=design_phases_list, dets=dets
    )

    internal_data = calc.clean_internal_data(
        internal_data=internal_data,
        column_value_replace=column_value_replace,
        public_dataset_column_renaming=public_dataset_column_renaming,
        metadata_col_order=internal_data_col_order,
    )

    calc.write_internal_data_to_excel(
        internal_data=internal_data,
        public_dataset_directory=internal_directory,
    )
    internal_data_logger.info("Internal data created.")


if __name__ == "__main__":
    create_internal_data()

# pylint: disable=E1130, W0718, C0103
"""Cleans raw tally and oneclick models."""

from pathlib import Path
from logging import getLogger
from wblca_benchmark_v2_data_prep.utils.loggers import setup_logger
import wblca_benchmark_v2_data_prep.lca_results.clean as clean_util
import wblca_benchmark_v2_data_prep.utils.general as general_util


def clean_raw_tally_files():
    """Clean raw tally files for further analysis.

    This script does the following:

    - Reads tally files in raw directory
    - Cleans tally files
    - adjusts the csi division of tally walls
    - writes tally files to cleaned directory
    """
    current_file_path = Path(__file__)
    main_directory = current_file_path.parents[2]
    raw_tally_directory = main_directory.joinpath("data/lca_results/raw/tally")
    cleaned_tally_directory = main_directory.joinpath("data/lca_results/cleaned/tally")

    # instantiate logger
    setup_logger(
        log_file_path=main_directory.joinpath(
            "data/logs/lca_results/clean_lca_results_tally.log"
        ),
        level="info",
    )

    main_clean_logger = getLogger("1_clean_script")
    main_clean_logger.info("Logger has been set up.")

    for tally_file in raw_tally_directory.glob("*.csv"):
        main_clean_logger.info("Begin cleaning of %s", tally_file.stem)
        # read tally files
        tally_df = general_util.read_csv(tally_file)

        tally_df = clean_util.clean_tally_df(tally_df=tally_df, tally_file=tally_file)

        adjusted_tally_df = clean_util.adjust_tally_walls(tally_df)

        general_util.write_to_csv(
            adjusted_tally_df, cleaned_tally_directory, tally_file.stem
        )
        main_clean_logger.info("End cleaning of %s", tally_file.stem)


def clean_raw_oneclick_files():
    """Clean raw One Click LCA files for further analysis.

    This script does the following:

    - Reads oneclick files in raw directory
    - Cleans oneclick files
    - writes oneclick files to cleaned directory
    """
    current_file_path = Path(__file__)
    main_directory = current_file_path.parents[2]
    raw_oneclick_directory = main_directory.joinpath("data/lca_results/raw/oneclick")
    cleaned_oneclick_directory = main_directory.joinpath(
        "data/lca_results/cleaned/oneclick"
    )

    # instantiate logger
    setup_logger(
        log_file_path=main_directory.joinpath(
            "data/logs/lca_results/clean_lca_results_oneclick.log"
        ),
        level="info",
    )

    main_clean_logger = getLogger("1_clean_script")
    main_clean_logger.info("Logger has been set up.")

    for oneclick_file in raw_oneclick_directory.glob("*.xlsx"):
        main_clean_logger.info("Begin cleaning of %s", oneclick_file.stem)
        # read oneclick files
        oneclick_df = clean_util.read_excel(oneclick_file)

        oneclick_df = clean_util.clean_oneclick_df(
            oneclick_df=oneclick_df, oneclick_file=oneclick_file
        )

        general_util.write_to_csv(
            oneclick_df, cleaned_oneclick_directory, oneclick_file.stem
        )
        main_clean_logger.info("End cleaning of %s", oneclick_file.stem)


if __name__ == "__main__":
    clean_raw_tally_files()
    clean_raw_oneclick_files()

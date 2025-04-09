# pylint: disable=C0103,
"""Combines tally and oneclick models into tool specific files."""
from pathlib import Path
from logging import getLogger
import pandas as pd
from wblca_benchmark_v2_data_prep.utils.loggers import setup_logger


def combine(directory_to_read: Path, write_directory: Path) -> None:
    """Combines all models in either tally or oneclick folders.

    Args:
        directory_to_read (Path): directory with all models
        write_directory (Path): location to save combined models
    """
    df_list = []
    for file in directory_to_read.glob("*.csv"):
        temp_df = pd.read_csv(file)
        df_list.append(temp_df)

    if len(df_list) > 0:
        final_df = pd.concat(df_list)
        final_df.to_csv(write_directory, index=False)


if __name__ == "__main__":
    current_file_path = Path(__file__)
    main_directory = current_file_path.parents[2]
    tally_directory_to_read = main_directory.joinpath("data/lca_results/ref_ele_mapped/tally")
    tally_write_path = main_directory.joinpath(
        "data/lca_results/combined/Tally_Model_Combined.csv"
    )
    oneclick_directory_to_read = main_directory.joinpath(
        "data/lca_results/ref_ele_mapped/oneclick"
    )
    oneclick_write_path = main_directory.joinpath(
        "data/lca_results/combined/OneClick_Model_Combined.csv"
    )
    setup_logger(
        log_file_path=main_directory.joinpath("data/logs/lca_results/combine_lca_results.log"),
        level="info",
    )

    main_combine_logger = getLogger("6_combine_script")
    main_combine_logger.info("Logger has been set up.")

    main_combine_logger.info("Combine tally files.")
    combine(tally_directory_to_read, tally_write_path)
    main_combine_logger.info("Combine oneclick files.")
    combine(oneclick_directory_to_read, oneclick_write_path)

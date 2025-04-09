# pylint: disable=C0103, R0801, R0914, R0915
"""Harmonize tally and one click files."""
from pathlib import Path
from logging import getLogger
import pandas as pd
import wblca_benchmark_v2_data_prep.utils.general as utils
from wblca_benchmark_v2_data_prep.utils.loggers import setup_logger


def harmonize():
    """
    Harmonizes tally and one click WBLCA outputs

    This function does the following:

    - Reads combined tally and oneclick files.
    - Removes and renames columns in both files.
    - Replaces values based on config file.
    - Fills nulls for impacts and mass values.
    - Combines tally and oneclick files into one harmonized file.
    Writes all to harmonized directory.
    """
    # set file path locations
    current_file_path = Path(__file__)
    main_directory = current_file_path.parents[2]
    setup_logger(
        log_file_path=main_directory.joinpath("data/logs/lca_results/harmonize_lca_results.log"),
        level="info",
    )

    main_harmonize_logger = getLogger("7_harmonize_script")
    main_harmonize_logger.info("Logger has been set up.")

    main_harmonize_logger.info("Begin configuration.")
    tally_combined_path = main_directory.joinpath(
        "data/lca_results/combined/Tally_Model_Combined.csv"
    )
    oneclick_combined_path = main_directory.joinpath(
        "data/lca_results/combined/OneClick_Model_Combined.csv"
    )
    harmonized_write_path = main_directory.joinpath("data/lca_results/harmonized")
    data_record_write_path = main_directory.joinpath("data/data_record/raw")
    config_path = main_directory.joinpath("references/config_harmonize.yml")

    # read config file
    config = utils.read_yaml(config_path)
    assert config is not None, "The config dictionary could not be set"

    column_removal_tally = config.get("column_removal_tally")
    assert (
        column_removal_tally is not None
    ), "The list for column removal for Tally could not \
be set"

    column_rename_tally = config.get("column_rename_tally")
    assert (
        column_rename_tally is not None
    ), "The dict for column renaming for Tally could not \
be set"

    column_removal_oneclick = config.get("column_removal_oneclick")
    assert (
        column_removal_oneclick is not None
    ), "The list for column removal for One Click \
could not be set"

    column_rename_oneclick = config.get("column_rename_oneclick")
    assert (
        column_rename_oneclick is not None
    ), "The dict for column renaming for One Click \
could not be set"

    column_null_replacement = config.get("column_null_replacement")
    assert (
        column_null_replacement is not None
    ), "The list for column null replacement \
could not be set"
    main_harmonize_logger.info("End configuration.")

    # read combined files
    main_harmonize_logger.info("Read combined lca_results files.")

    combined_tally_adjusted = None
    combined_oneclick_adjusted = None
    # Combined Tally
    try:
        combined_tally = utils.read_csv(tally_combined_path)
        # get the combined sets of columns to drop
        tally_columns_to_drop = list(
            set(combined_tally.columns.to_list()) & set(column_removal_tally)
        )
        combined_tally_adjusted = (
            combined_tally.rename(columns=column_rename_tally)
            .drop(columns=tally_columns_to_drop)
            .set_index("CLF Model ID")
        )

        for df_key, value_to_replace_dict in config.get("column_value_replace_tally").items():
            combined_tally_adjusted[df_key] = combined_tally_adjusted[df_key].replace(
                value_to_replace_dict
            )
        for col_null_replace in column_null_replacement:
            combined_tally_adjusted[col_null_replace] = combined_tally_adjusted[
                col_null_replace
            ].fillna(0)
        utils.write_to_csv(combined_tally_adjusted, harmonized_write_path, "tally_harmonized")
    except Exception:
        print(f"Unable to complete harmonization for tally files: {Exception}")

    try:
        combined_oneclick = utils.read_csv(oneclick_combined_path)
        oneclick_columns_to_drop = list(
            set(combined_oneclick.columns.to_list()) & set(column_removal_oneclick)
        )
        combined_oneclick_adjusted = (
            combined_oneclick.rename(columns=column_rename_oneclick)
            .drop(columns=oneclick_columns_to_drop)
            .set_index("CLF Model ID")
        )
        for df_key, value_to_replace_dict in config.get("column_value_replace_oneclick").items():
            combined_oneclick_adjusted[df_key] = combined_oneclick_adjusted[df_key].replace(
                value_to_replace_dict
            )
        for col_null_replace in column_null_replacement:
            combined_oneclick_adjusted[col_null_replace] = combined_oneclick_adjusted[
                col_null_replace
            ].fillna(0)
        utils.write_to_csv(
            combined_oneclick_adjusted, harmonized_write_path, "oneclick_harmonized"
        )
    except Exception:
        print(f"Unable to complete harmonization for oneclick files: {Exception}")

    # Combine the dataframes, handling cases where one might not exist
    combined_raw_wblca_output = None
    try:
        if combined_tally_adjusted is not None and combined_oneclick_adjusted is not None:
            combined_raw_wblca_output = pd.concat(
                [combined_tally_adjusted, combined_oneclick_adjusted], join="outer"
            )
            print("Combined both tally and oneclick dataframes")
        elif combined_tally_adjusted is not None:
            combined_raw_wblca_output = combined_tally_adjusted
            print("Using only tally dataframe as oneclick is not available")
        elif combined_oneclick_adjusted is not None:
            combined_raw_wblca_output = combined_oneclick_adjusted
            print("Using only oneclick dataframe as tally is not available")
        else:
            combined_raw_wblca_output = None
            print("No dataframes available to combine")

        # write to csv
        if combined_raw_wblca_output is not None:
            utils.write_to_csv(
                combined_raw_wblca_output, harmonized_write_path, "combined_harmonized"
            )
            utils.write_to_csv(
                combined_raw_wblca_output, data_record_write_path, "combined_harmonized"
            )
    except Exception:
        print(f"unable to combined outputs for raw wblca output: {Exception}")


if __name__ == "__main__":
    harmonize()

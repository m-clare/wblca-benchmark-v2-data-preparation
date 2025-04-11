"""utils for calculating public dataset values"""

from pathlib import Path
import pandas as pd
from logging import getLogger
from wblca_benchmark_v2_data_prep.data_record.output_format import format_internal_data

internal_data_logger = getLogger("data_record.internal_data_calcs")


def create_internal_data(
    accepted_design_phases: list, dets: pd.DataFrame
) -> pd.DataFrame:
    """First step to create internal dataset.

    This function does the following:
    - Sorts vales by climate zone.
    - Filters out projects that are not final reports.
    - Filters out projects that are not DD or later.
    - Sets index to 'CLF Model ID"

    Args:
        accepted_design_phases (list): list of design phases to be used.
        dets (pd.DataFrame): project metadata created by metadata scripts.

    Returns:
        pd.DataFrame: dataframe of internal data.
    """
    internal_data_logger.info("Begin creating internal data.")
    internal_data = dets.sort_values(by="clim_zone")
    internal_data = (
        internal_data.loc[internal_data["final_report"] == "Yes"]
        .loc[internal_data["design_phase"].isin(accepted_design_phases)]
        .set_index("clf_model_id")
    )
    internal_data_logger.info("End creating internal data.")

    return internal_data


def clean_internal_data(
    internal_data: pd.DataFrame,
    column_value_replace: dict,
    public_dataset_column_renaming: dict,
    metadata_col_order: list,
) -> pd.DataFrame:
    """Cleans internal data for future use.

    This function does the following:
    - Reorders columns into order for data record.
    - Replaces field values (mostly related to building use type)
    - Renames columns based on config file.
    - Renumbers index to be more human readable.

    Args:
        internal_data (pd.DataFrame): Internal data created in create_internal_data function.
        column_value_replace (dict): dictionary of column values to replace.
        public_dataset_column_renaming (dict): dictionary of column names for replacement.
        metadata_col_order (list): Order of columns for data record.

    Returns:
        pd.DataFrame: Internal data for data record use.
    """
    internal_data_logger.info("Begin cleaning internal data.")
    internal_data = internal_data.reset_index()

    # reorder columns
    internal_data_logger.info("Reorder columns based on metadata_col_order.")
    internal_data = internal_data[metadata_col_order]

    # replace values
    internal_data_logger.info("Replace values based on column_value_replace.")
    for key, value in column_value_replace.items():
        internal_data[key] = internal_data[key].replace(value)

    # rename columns
    internal_data_logger.info(
        "Reename columns based on public_dataset_column_renaming."
    )
    internal_data = internal_data.rename(columns=public_dataset_column_renaming)

    internal_data.index = internal_data.index + 1
    internal_data_logger.info("End cleaning internal data.")

    return internal_data


def write_internal_data_to_excel(
    internal_data: pd.DataFrame, public_dataset_directory: Path
) -> None:
    """Writes internal data to excel. Name of file is fixed to internal_data.xlsx.

    Args:
        internal_data (pd.DataFrame): Internal data to be written to excel.
        public_dataset_directory (Path): Target path of internal data.
    """
    with pd.ExcelWriter(
        public_dataset_directory.joinpath("internal_data.xlsx")
    ) as writer:
        internal_data.to_excel(
            writer,
            sheet_name="project metadata",
            index_label="project_index",
        )

        format_internal_data(writer=writer)
        internal_data_logger.info(
            "Internal data has beeen saved to %s", public_dataset_directory
        )

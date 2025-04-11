# pylint: disable=E1130, W0718, C0103
"""Module that implements element mapping for Tally and One Click LCA"""

from pathlib import Path
from logging import getLogger
from wblca_benchmark_v2_data_prep.lca_results.MappingImplementation import (
    TallyRefinedElementMapper,
    OneClickRefinedElementMapper,
)
import wblca_benchmark_v2_data_prep.lca_results.comb_refined_ele_filters as ref
import wblca_benchmark_v2_data_prep.utils.general as gen
from wblca_benchmark_v2_data_prep.utils.loggers import setup_logger


def map_tally_elements_refined():
    """Maps Tally elements a second time.

    This script does the following:

    - Reads in the tally file.
    - Instatiates the refined element mapper.
    - filters the tally file based on material mapping that has occured.
    - Writes the file to the ref_ele_mapped directory.
    """
    current_file_path = Path(__file__)
    main_directory = current_file_path.parents[2]
    mat_mapped_tally_directory = main_directory.joinpath(
        "data/lca_results/material_mapped/tally"
    )

    setup_logger(
        log_file_path=main_directory.joinpath(
            "data/logs/lca_results/map_elements_refined_lca_results_tally.log"
        ),
        level="info",
    )

    main_map_ele_ref_logger = getLogger("5_map_elements_refined_script")
    main_map_ele_ref_logger.info("Logger has been set up.")

    for tally_file in mat_mapped_tally_directory.glob("*.csv"):
        main_map_ele_ref_logger.info(
            "Begin mapping elements in a refined method for %s", tally_file.name
        )
        # read combined tally files
        tally_df = gen.read_csv(tally_file)

        # instantiate ElementMapper
        Mapper = TallyRefinedElementMapper(
            tally_df, ref.RefinedElementFilter("CLF Omni")
        )
        Mapper.do_filtering()

        Mapper.write_csv(
            main_directory.joinpath(
                f"data/lca_results/ref_ele_mapped/tally/{tally_file.stem}_RefMapped.csv"
            )
        )
        # Mapper.write_pickle()


def map_oneclick_elements_refined():
    """Maps One Click elements a second time.

    This script does the following:

    - Reads in the oneclick file.
    - Instatiates the refined element mapper.
    - filters the oneclick file based on material mapping that has occured.
    - Writes the file to the ref_ele_mapped directory.
    """
    current_file_path = Path(__file__)
    main_directory = current_file_path.parents[2]
    cleaned_oneclick_directory = main_directory.joinpath(
        "data/lca_results/material_mapped/oneclick"
    )

    setup_logger(
        log_file_path=main_directory.joinpath(
            "data/logs/lca_results/map_elements_refined_lca_results_oneclick.log"
        ),
        level="info",
    )

    main_map_ele_ref_logger = getLogger("5_map_elements_refined_script")
    main_map_ele_ref_logger.info("Logger has been set up.")

    for oneclick_file in cleaned_oneclick_directory.glob("*.csv*"):
        main_map_ele_ref_logger.info(
            "Begin mapping elements in a refined method for %s", oneclick_file.name
        )
        oneclick_df = gen.read_csv(oneclick_file)

        Mapper = OneClickRefinedElementMapper(
            oneclick_df, ref.RefinedElementFilter("CLF Omni")
        )
        Mapper.do_filtering()

        Mapper.write_csv(
            main_directory.joinpath(
                f"data/lca_results/ref_ele_mapped/oneclick/{oneclick_file.stem}_EleMapped.csv"
            )
        )
        # Mapper.write_pickle()


if __name__ == "__main__":
    map_tally_elements_refined()
    map_oneclick_elements_refined()

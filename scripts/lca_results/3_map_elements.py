# pylint: disable=E1130, W0718, C0103
"""Module that implements element mapping for Tally and One Click LCA"""

from pathlib import Path
from logging import getLogger
from wblca_benchmark_v2_data_prep.lca_results.MappingImplementation import (
    TallyElementMapper,
    OneClickElementMapper,
)
import wblca_benchmark_v2_data_prep.lca_results.oneclick_ele_filters as oc_fi
import wblca_benchmark_v2_data_prep.lca_results.tally_ele_filters as t_fi
import wblca_benchmark_v2_data_prep.utils.general as gen
from wblca_benchmark_v2_data_prep.utils.loggers import setup_logger


def map_tally_elements():
    """Maps Tally elements.

    This script does the following:

    - Instantiates filters created in tally_ele_filters
    - Reads tally files
    - Instantiates a mapper object
    - Loops through the filters and applies them to the tally file
    - Writes the element mapped file to the element_mapped directory
    """
    current_file_path = Path(__file__)
    main_directory = current_file_path.parents[2]
    ex_bio_tally_directory = main_directory.joinpath("data/lca_results/csc/")

    # instantiate logger
    setup_logger(
        log_file_path=main_directory.joinpath(
            "data/logs/lca_results/map_elements_lca_results_tally.log"
        ),
        level="info",
    )

    main_map_ele_logger = getLogger("3_map_elements_script")
    main_map_ele_logger.info("Logger has been set up.")

    tally_filters = [
        t_fi.CurtainWallPanels("CLF Omni"),
        t_fi.CurtainWallMullions("CLF Omni"),
        t_fi.Doors("CLF Omni"),
        t_fi.Floors("CLF Omni"),
        t_fi.Roofs("CLF Omni"),
        t_fi.Railings("CLF Omni"),
        t_fi.Stairs("CLF Omni"),
        t_fi.StructuralColumns("CLF Omni"),
        t_fi.StructuralConnections("CLF Omni"),
        t_fi.StructuralFoundations("CLF Omni"),
        t_fi.StructuralFraming("CLF Omni"),
        t_fi.Walls("CLF Omni"),
        t_fi.Windows("CLF Omni"),
    ]

    for tally_file in ex_bio_tally_directory.glob("*.csv"):
        main_map_ele_logger.info("Begin mapping elements for %s", tally_file.name)
        # read combined tally files
        tally_df = gen.read_csv(tally_file)

        # instantiate ElementMapper
        Mapper = TallyElementMapper(tally_df, t_fi.Ceilings("CLF Omni"))
        Mapper.do_filtering()

        for fil in tally_filters:
            Mapper.change_filter_type(fil)
            Mapper.do_filtering()

        Mapper.write_csv(
            main_directory.joinpath(
                f"data/lca_results/element_mapped/tally/{tally_file.stem}_EleMapped.csv"
            )
        )
        main_map_ele_logger.info("Elements mapped for %s.", tally_file.name)
        # Mapper.write_pickle()


def map_oneclick_elements():
    """Maps oneclick elements.

    This script does the following:

    - Instantiates filters created in oneclick_ele_filters
    - Reads oneclick files
    - Instantiates a mapper object
    - Loops through the filters and applies them to the oneclick file
    - Writes the element mapped file to the element_mapped directory
    """
    current_file_path = Path(__file__)
    main_directory = current_file_path.parents[2]
    # combined_oneclick_path_pkl = main_directory.joinpath('data/combined/combined_oneclick.pkl')
    cleaned_oneclick_directory = main_directory.joinpath(
        "data/lca_results/cleaned/oneclick"
    )

    # instantiate logger
    setup_logger(
        log_file_path=main_directory.joinpath(
            "data/logs/lca_results/map_elements_lca_results_oneclick.log"
        ),
        level="info",
    )

    main_map_ele_logger = getLogger("3_map_elements_script")
    main_map_ele_logger.info("Logger has been set up.")

    oneclick_filters = [
        oc_fi.OmniClassShellSuperstructure("CLF Omni"),
        oc_fi.OmniClassShellEnclosure("CLF Omni"),
        oc_fi.OmniClassInteriorConstruction("CLF Omni"),
        oc_fi.OmniClassInteriorFinishes("CLF Omni"),
        oc_fi.OmniClassMEP("CLF Omni"),
        oc_fi.OmniClassNotDefined("CLF Omni"),
        oc_fi.CSIDivision("CLF Omni"),
    ]

    for oneclick_file in cleaned_oneclick_directory.glob("*.csv*"):
        main_map_ele_logger.info("Begin mapping elements for %s", oneclick_file.name)
        oneclick_df = gen.read_csv(oneclick_file)

        Mapper = OneClickElementMapper(
            oneclick_df, oc_fi.OmniClassSubstructure("CLF Omni")
        )
        Mapper.do_filtering()

        for fil in oneclick_filters:
            Mapper.change_filter_type(fil)
            Mapper.do_filtering()

        Mapper.write_csv(
            main_directory.joinpath(
                f"data/lca_results/element_mapped/oneclick/{oneclick_file.stem}_EleMapped.csv"
            )
        )
        main_map_ele_logger.info("Elements mapped for %s.", oneclick_file.name)
        # Mapper.write_pickle()


if __name__ == "__main__":
    map_tally_elements()
    map_oneclick_elements()

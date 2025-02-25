# pylint: disable=E1130, W0718, C0103
"""Module that implements element mapping for Tally and One Click LCA"""
from pathlib import Path
from logging import getLogger
from wblca_benchmark_v2_data_prep.lca_results.MappingImplementation import \
    TallyMaterialQuantityMapper, OneClickMaterialQuantityMapper
import wblca_benchmark_v2_data_prep.lca_results.oneclick_mat_filters as oc_fi
import wblca_benchmark_v2_data_prep.lca_results.tally_mat_filters as t_fi
import wblca_benchmark_v2_data_prep.utils.general as gen
from wblca_benchmark_v2_data_prep.utils.loggers import setup_logger


def map_tally_materials():
    """Maps Tally materials.

    This script does the following:
    - creates the filter classes required for material mapping
    - reads in each element mapped tally file
    - Completes material mapping for field "MQ_1"
    - Uses the updated dataframe to map materials for field "MQ_2"
    - Uses the updated dataframe to map materials to "MQ_1" assuming that "MQ_1" is "Other".
        This is done because some rules required a first level of filtering.
    - Uses the updated dataframe to map materials to "MQ_2" assuming that "MQ_1" is "Other".
    - Uses the updated dataframe to map MQ_2 values that are other to a more material
        specific other category (e.g. Concrete - other)
    - writes newly updated tally file to material_mapped directory
    """
    current_file_path = Path(__file__)
    main_directory = current_file_path.parents[2]
    ele_mapped_tally_directory = main_directory.joinpath('data/lca_results/element_mapped/tally')

    setup_logger(
        log_file_path=main_directory.joinpath(
            'data/logs/lca_results/map_materials_lca_results_tally.log'
        ),
        level='info'
    )

    main_map_mat_logger = getLogger('4_map_materials_script')
    main_map_mat_logger.info('Logger has been set up.')

    tally_material_quantity_one_filters = [
        t_fi.ConcreteMaterialQuantityOne('MQ_1'),
        t_fi.SteelMaterialQuantityOne('MQ_1'),
        t_fi.MasonryMaterialQuantityOne('MQ_1'),
        t_fi.AluminumMaterialQuantityOne('MQ_1'),
        t_fi.WoodMaterialQuantityOne('MQ_1'),
        t_fi.GlazingMaterialQuantityOne('MQ_1'),
        t_fi.RoofMaterialQuantityOne('MQ_1'),
        t_fi.InsulationMaterialQuantityOne('MQ_1'),
        t_fi.GypsumMaterialQuantityOne('MQ_1'),
        t_fi.FireproofMaterialQuantityOne('MQ_1'),
    ]
    tally_material_quantity_two_filters = [
        t_fi.ConcreteMaterialQuantityTwo('MQ_2'),
        t_fi.SteelMaterialQuantityTwo('MQ_2'),
        t_fi.MasonryMaterialQuantityTwo('MQ_2'),
        t_fi.AluminumMaterialQuantityTwo('MQ_2'),
        t_fi.WoodMaterialQuantityTwo('MQ_2'),
        t_fi.GlazingMaterialQuantityTwo('MQ_2'),
        t_fi.RoofMaterialQuantityTwo('MQ_2'),
        t_fi.InsulationMaterialQuantityTwo('MQ_2'),
        t_fi.GypsumMaterialQuantityTwo('MQ_2'),
        t_fi.FireproofMaterialQuantityTwo('MQ_2'),
    ]
    tally_material_quantity_one_other_filters = [
        t_fi.DoorFrameMaterialQuantityOneOther('MQ_1'),
        t_fi.WindowFrameMaterialQuantityOneOther('MQ_1'),
        t_fi.AcousticCeilingsMaterialQuantityOneOther('MQ_1'),
        t_fi.SyntheticCompositesMaterialQuantityOneOther('MQ_1'),
        t_fi.CladdingMaterialQuantityOneOther('MQ_1'),
        t_fi.AdhesivesMaterialQuantityOneOther('MQ_1'),
        t_fi.AirVaporMaterialQuantityOneOther('MQ_1'),
        t_fi.CoatingsMaterialQuantityOneOther('MQ_1'),
        t_fi.FloorTileMaterialQuantityOneOther('MQ_1'),
        t_fi.WallCoveringsMaterialQuantityOneOther('MQ_1'),
        t_fi.OtherMetalsMaterialQuantityOneOther('MQ_1'),
    ]
    tally_material_quantity_two_other_filters = [
        t_fi.DoorFrameMaterialQuantityTwoOther('MQ_2'),
        t_fi.WindowFrameMaterialQuantityTwoOther('MQ_2'),
        t_fi.AcousticCeilingsMaterialQuantityTwoOther('MQ_2'),
        t_fi.SyntheticCompositesMaterialQuantityTwoOther('MQ_2'),
        t_fi.CladdingMaterialQuantityTwoOther('MQ_2'),
        t_fi.AdhesivesMaterialQuantityTwoOther('MQ_2'),
        t_fi.AirVaporMaterialQuantityTwoOther('MQ_2'),
        t_fi.CoatingsMaterialQuantityTwoOther('MQ_2'),
        t_fi.FloorTileMaterialQuantityTwoOther('MQ_2'),
        t_fi.OtherMetalsMaterialQuantityTwoOther('MQ_2'),
    ]
    tally_material_quantity_two_unique_other_filters = [
        t_fi.FinalOtherMaterialQuantityTwoOther('MQ_2')
    ]

    for tally_file in ele_mapped_tally_directory.glob('*.csv'):
        main_map_mat_logger.info('Begin mapping materials for %s', tally_file.name)
        # read combined tally files
        tally_df = gen.read_csv(tally_file)

        # instantiate Material Mapper for Material Quantity One
        main_map_mat_logger.info('Working on MQ_1 of %s', tally_file.name)
        MaterialQuantityOneMapper = TallyMaterialQuantityMapper(
            tally_df,
        )

        for fil in tally_material_quantity_one_filters:
            MaterialQuantityOneMapper.change_filter_type(fil)
            MaterialQuantityOneMapper.do_filtering()

        material_quantity_one_updated_tally_df = MaterialQuantityOneMapper.df

        main_map_mat_logger.info('Working on MQ_2 of %s', tally_file.name)
        # instantiate Material Mapper for Material Quantity Two using updated df
        MaterialQuantityTwoMapper = TallyMaterialQuantityMapper(
            material_quantity_one_updated_tally_df,
        )

        for fil in tally_material_quantity_two_filters:
            MaterialQuantityTwoMapper.change_filter_type(fil)
            MaterialQuantityTwoMapper.do_filtering()

        mq_one_and_two_updated_tally_df = MaterialQuantityTwoMapper.df

        main_map_mat_logger.info('Working on MQ_1 of %s to sort Other Materials', tally_file.name)
        # instantiate Material Mapper for Material Quantity one of other materials using updated df
        MaterialQuantityOneOtherMapper = TallyMaterialQuantityMapper(
            mq_one_and_two_updated_tally_df,
        )

        for fil in tally_material_quantity_one_other_filters:
            MaterialQuantityOneOtherMapper.change_filter_type(fil)
            MaterialQuantityOneOtherMapper.do_filtering()

        mq_one_two_and_other_one_updated_tally_df = MaterialQuantityOneOtherMapper.df

        main_map_mat_logger.info('Working on MQ_2 of %s to sort Other Materials', tally_file.name)
        # instantiate Material Mapper for Material Quantity Two using updated df
        MaterialQuantityTwoOtherMapper = TallyMaterialQuantityMapper(
            mq_one_two_and_other_one_updated_tally_df,
        )

        for fil in tally_material_quantity_two_other_filters:
            MaterialQuantityTwoOtherMapper.change_filter_type(fil)
            MaterialQuantityTwoOtherMapper.do_filtering()

        mq_one_two_and_other_one_two_updated_tally_df = MaterialQuantityTwoOtherMapper.df

        main_map_mat_logger.info('Working on MQ_2 of %s to replace Other values', tally_file.name)
        # instantiate Material Mapper for Material Quantity Two using updated df
        MaterialQuantityTwoFinalOtherMapper = TallyMaterialQuantityMapper(
            mq_one_two_and_other_one_two_updated_tally_df,
        )

        for fil in tally_material_quantity_two_unique_other_filters:
            MaterialQuantityTwoFinalOtherMapper.change_filter_type(fil)
            MaterialQuantityTwoFinalOtherMapper.do_filtering()

        # write to csv
        MaterialQuantityTwoFinalOtherMapper.write_csv(
            main_directory.joinpath(
                f'data/lca_results/material_mapped/tally/{tally_file.stem}_MatMapped.csv'
            )
        )
        # Mapper.write_pickle()


def map_oneclick_materials():
    """Maps One Click materials.

    This script does the following:
    - creates the filter classes required for material mapping
    - reads in each element mapped oneclick file
    - Completes material mapping for field "MQ_1"
    - Uses the updated dataframe to map materials for field "MQ_2"
    - Uses the updated dataframe to map materials to "MQ_1" assuming that "MQ_1" is "Other".
        This is done because some rules required a first level of filtering.
    - Uses the updated dataframe to map materials to "MQ_2" assuming that "MQ_1" is "Other".
    - Uses the updated dataframe to map MQ_2 values that are other to a more material
        specific other category (e.g. Concrete - other)
    - writes newly updated oneclick file to material_mapped directory
    """
    current_file_path = Path(__file__)
    main_directory = current_file_path.parents[2]
    ele_mapped_oneclick_directory = main_directory.joinpath(
        'data/lca_results/element_mapped/oneclick'
    )

    setup_logger(
        log_file_path=main_directory.joinpath(
            'data/logs/lca_results/map_materials_lca_results_oneclick.log'
        ),
        level='info'
    )

    main_map_mat_logger = getLogger('4_map_materials_script')
    main_map_mat_logger.info('Logger has been set up.')

    oneclick_material_quantity_one_filters = [
        oc_fi.ConcreteMaterialQuantityOne('MQ_1'),
        oc_fi.SteelMaterialQuantityOne('MQ_1'),
        oc_fi.MasonryMaterialQuantityOne('MQ_1'),
        oc_fi.AluminumMaterialQuantityOne('MQ_1'),
        oc_fi.WoodMaterialQuantityOne('MQ_1'),
        oc_fi.GlazingMaterialQuantityOne('MQ_1'),
        oc_fi.RoofMaterialQuantityOne('MQ_1'),
        oc_fi.InsulationMaterialQuantityOne('MQ_1'),
        oc_fi.GypsumMaterialQuantityOne('MQ_1'),
        oc_fi.FireproofMaterialQuantityOne('MQ_1'),
    ]
    oneclick_material_quantity_two_filters = [
        oc_fi.ConcreteMaterialQuantityTwo('MQ_2'),
        oc_fi.SteelMaterialQuantityTwo('MQ_2'),
        oc_fi.MasonryMaterialQuantityTwo('MQ_2'),
        oc_fi.AluminumMaterialQuantityTwo('MQ_2'),
        oc_fi.WoodMaterialQuantityTwo('MQ_2'),
        oc_fi.GlazingMaterialQuantityTwo('MQ_2'),
        oc_fi.RoofMaterialQuantityTwo('MQ_2'),
        oc_fi.InsulationMaterialQuantityTwo('MQ_2'),
        oc_fi.GypsumMaterialQuantityTwo('MQ_2'),
        oc_fi.FireproofMaterialQuantityTwo('MQ_2'),
    ]
    oneclick_material_quantity_one_other_filters = [
        oc_fi.DoorFrameMaterialQuantityOneOther('MQ_1'),
        oc_fi.WindowFrameMaterialQuantityOneOther('MQ_1'),
        oc_fi.AcousticCeilingsMaterialQuantityOneOther('MQ_1'),
        oc_fi.SyntheticCompositesMaterialQuantityOneOther('MQ_1'),
        oc_fi.CladdingMaterialQuantityOneOther('MQ_1'),
        oc_fi.AdhesivesMaterialQuantityOneOther('MQ_1'),
        oc_fi.AirVaporMaterialQuantityOneOther('MQ_1'),
        oc_fi.CoatingsMaterialQuantityOneOther('MQ_1'),
        oc_fi.FloorTileMaterialQuantityOneOther('MQ_1'),
        oc_fi.OtherMetalsMaterialQuantityOneOther('MQ_1'),
        oc_fi.WallCoveringsMaterialQuantityOneOther('MQ_1')
    ]
    oneclick_material_quantity_two_other_filters = [
        oc_fi.DoorFrameMaterialQuantityTwoOther('MQ_2'),
        oc_fi.WindowFrameMaterialQuantityTwoOther('MQ_2'),
        oc_fi.AcousticCeilingsMaterialQuantityTwoOther('MQ_2'),
        oc_fi.SyntheticCompositesMaterialQuantityTwoOther('MQ_2'),
        oc_fi.CladdingMaterialQuantityTwoOther('MQ_2'),
        oc_fi.AdhesivesMaterialQuantityTwoOther('MQ_2'),
        oc_fi.AirVaporMaterialQuantityTwoOther('MQ_2'),
        oc_fi.CoatingsMaterialQuantityTwoOther('MQ_2'),
        oc_fi.FloorTileMaterialQuantityTwoOther('MQ_2'),
        oc_fi.OtherMetalsMaterialQuantityTwoOther('MQ_2'),
        oc_fi.ConcreteReadyMixMaterialQuantityTwo('MQ_2'),
    ]
    oneclick_material_quantity_two_unique_other_filters = [
        oc_fi.FinalOtherMaterialQuantityTwoOther('MQ_2')
    ]

    for oneclick_file in ele_mapped_oneclick_directory.glob('*.csv'):
        main_map_mat_logger.info('Begin mapping materials for %s', oneclick_file.name)
        # read combined tally files
        tally_df = gen.read_csv(oneclick_file)

        # instantiate Material Mapper for Material Quantity One
        main_map_mat_logger.info('Working on MQ_1 of %s', oneclick_file.name)
        MaterialQuantityOneMapper = OneClickMaterialQuantityMapper(
            tally_df,
        )

        for fil in oneclick_material_quantity_one_filters:
            MaterialQuantityOneMapper.change_filter_type(fil)
            MaterialQuantityOneMapper.do_filtering()

        material_quantity_one_updated_tally_df = MaterialQuantityOneMapper.df

        main_map_mat_logger.info('Working on MQ_2 of %s', oneclick_file.name)
        # instantiate Material Mapper for Material Quantity Two using updated df
        MaterialQuantityTwoMapper = OneClickMaterialQuantityMapper(
            material_quantity_one_updated_tally_df,
        )

        for fil in oneclick_material_quantity_two_filters:
            MaterialQuantityTwoMapper.change_filter_type(fil)
            MaterialQuantityTwoMapper.do_filtering()

        mq_one_and_two_updated_tally_df = MaterialQuantityTwoMapper.df

        main_map_mat_logger.info(
            'Working on MQ_1 of %s to sort Other Materials', oneclick_file.name
        )
        # instantiate Material Mapper for Material Quantity one of other materials using updated df
        MaterialQuantityOneOtherMapper = OneClickMaterialQuantityMapper(
            mq_one_and_two_updated_tally_df,
        )

        for fil in oneclick_material_quantity_one_other_filters:
            MaterialQuantityOneOtherMapper.change_filter_type(fil)
            MaterialQuantityOneOtherMapper.do_filtering()

        mq_one_two_and_other_one_updated_tally_df = MaterialQuantityOneOtherMapper.df

        main_map_mat_logger.info(
            'Working on MQ_2 of %s to sort Other Materials', oneclick_file.name
        )
        # instantiate Material Mapper for Material Quantity Two using updated df
        MaterialQuantityTwoOtherMapper = OneClickMaterialQuantityMapper(
            mq_one_two_and_other_one_updated_tally_df,
        )

        for fil in oneclick_material_quantity_two_other_filters:
            MaterialQuantityTwoOtherMapper.change_filter_type(fil)
            MaterialQuantityTwoOtherMapper.do_filtering()

        mq_one_two_and_other_one_two_updated_tally_df = \
            MaterialQuantityTwoOtherMapper.df

        main_map_mat_logger.info('Working on MQ_2 of %s to replace Other values', oneclick_file.name)
        # instantiate Material Mapper for Material Quantity Two using updated df
        MaterialQuantityTwoFinalOtherMapper = OneClickMaterialQuantityMapper(
            mq_one_two_and_other_one_two_updated_tally_df,
        )

        for fil in oneclick_material_quantity_two_unique_other_filters:
            MaterialQuantityTwoFinalOtherMapper.change_filter_type(fil)
            MaterialQuantityTwoFinalOtherMapper.do_filtering()

        # write to csv
        MaterialQuantityTwoFinalOtherMapper.write_csv(
            main_directory.joinpath(
                f'data/lca_results/material_mapped/oneclick/{oneclick_file.stem}_MatMapped.csv'
            )
        )
        # Mapper.write_pickle()


if __name__ == '__main__':
    map_tally_materials()
    map_oneclick_materials()

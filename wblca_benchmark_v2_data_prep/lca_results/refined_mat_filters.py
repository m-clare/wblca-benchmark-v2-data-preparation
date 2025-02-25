"""Creates dictionaries of filters for refined element mapping."""
from typing import Dict
import pandas as pd
from wblca_benchmark_v2_data_prep.lca_results.enums import \
    MaterialQuantityOne, MaterialQuantityTwo, OmniClassLevelOne


def create_all_refined_filters(df: pd.DataFrame) -> Dict[str, pd.Series]:
    """Creates a dictionary of filters to be implemented for refined element mapping.

    Args:
        df (pd.DataFrame): DataFrame of entries

    Returns:
        Dict[str, pd.Series]: dictionary of filters
    """
    filters = {
        'acous_ceilings_mq_one': df['MQ_1'].str.fullmatch(
            MaterialQuantityOne.ACOUSTIC_CEILINGS.value
        ),
        'vapor_barrier_mq_one': df['MQ_1'].str.fullmatch(MaterialQuantityOne.AIR_VAPOR.value),
        'cladding_mq_one': df['MQ_1'].str.fullmatch(MaterialQuantityOne.CLADDING.value),
        'floor_tile_mq_one': df['MQ_1'].str.fullmatch(MaterialQuantityOne.FLOOR.value),
        'insulation_mq_one': df['MQ_1'].str.fullmatch(MaterialQuantityOne.INSULATION.value),
        'conc_mq_one': df['MQ_1'].str.fullmatch(MaterialQuantityOne.CONCRETE.value),
        'masonry_mq_one': df['MQ_1'].str.fullmatch(MaterialQuantityOne.MASONRY.value),
        'door_mq_one': df['MQ_1'].str.fullmatch(MaterialQuantityOne.DOOR_FRAME.value),
        'glazing_mq_one': df['MQ_1'].str.fullmatch(MaterialQuantityOne.GLAZING.value),
        'roofing_mq_one': df['MQ_1'].str.fullmatch(MaterialQuantityOne.ROOF.value),
        'windows_mq_one': df['MQ_1'].str.fullmatch(MaterialQuantityOne.WINDOW_FRAME.value),
        'raised_access_mq_two': df['MQ_2'].str.fullmatch(
            MaterialQuantityTwo.RAISED_ACESS_FLOOR.value
        ),
        'clt_mq_two': df['MQ_2'].str.fullmatch(MaterialQuantityTwo.CLT.value),
        'glt_mq_two': df['MQ_2'].str.fullmatch(MaterialQuantityTwo.GLT.value),
        'wood_i_joist_mq_two': df['MQ_2'].str.fullmatch(MaterialQuantityTwo.WOOD_I_JOIST.value),
        'heavy_timber_mq_two': df['MQ_2'].str.fullmatch(MaterialQuantityTwo.HEAVY_TIMBER.value),
        'hot_rolled_mq_two': df['MQ_2'].str.fullmatch(MaterialQuantityTwo.HOT_ROLLED.value),
        'deck_mq_two': df['MQ_2'].str.fullmatch(MaterialQuantityTwo.DECK.value),
        'gypsum_board_mq_two': df['MQ_2'].str.fullmatch(MaterialQuantityTwo.INT_GYPSUM.value),
        'ready_mix_lw_mq_two': df['MQ_2'].str.contains('Ready mix LW'),
        'wood_door_mq_two': df['MQ_2'].str.fullmatch(MaterialQuantityTwo.WOOD_DOOR.value),
        'wood_door_frame_mq_two': df['MQ_2'].str.fullmatch(
            MaterialQuantityTwo.WOOD_DOOR_FRAME.value
        ),
        'superstructure_cat_ele_one': df['CLF Omni'].str.fullmatch(
            OmniClassLevelOne.SUPERSTRUCTURE.value
        ),
        'finishes_cat_ele_one': df['CLF Omni'].str.fullmatch(
            OmniClassLevelOne.INTERIOR_FINISHES.value
        ),
        'unknown_cat_ele_one': df['CLF Omni'].str.fullmatch(OmniClassLevelOne.UNKNOWN.value)
    }

    return filters

"""Creates dictionaries of filters for element mapping."""

from typing import Dict
import pandas as pd


def create_all_oneclick_filters(df: pd.DataFrame) -> Dict[str, pd.Series]:
    """Creates a dictionary of One Click filters to be implemented.

    Args:
        df (pd.DataFrame): DataFrame of One Click entries

    Returns:
        Dict[str, pd.Series]: dictionary of One Click filters
    """
    filters = {
        "oc_clf_omni_na": pd.isna(df["CLF Omni"]),
        "oc_omni_sub": df["Omniclass"].str.match("21-01"),
        "oc_omni_shell_super": df["Omniclass"].str.match("21-02 1"),
        "oc_omni_shell_enc": df["Omniclass"].str.match("21-02 2|21-02 3"),
        "oc_omni_int_con": df["Omniclass"].str.match("21-03 1"),
        "oc_omni_int_fin": df["Omniclass"].str.match("21-03 2"),
        "oc_omni_mep": df["Omniclass"].str.match("21-04|21-05"),
        "oc_omni_nd": df["Omniclass"].str.fullmatch("Not defined"),
        "oc_q_fdn": df["Question"].str.fullmatch(
            "Foundation, sub-surface, basement and retaining walls"
        ),
        "oc_q_vert": df["Question"].str.fullmatch(
            "Columns and load-bearing vertical structures"
        ),
        "oc_q_horz": df["Question"].str.fullmatch(
            "Floor slabs, ceilings, roofing decks, beams and roof"
        ),
        "oc_q_other": df["Question"].str.fullmatch("Other structures and materials"),
        "oc_q_ext": df["Question"].str.fullmatch("External walls and facade"),
        "oc_q_int": df["Question"].str.fullmatch(
            "Internal walls and non-bearing structures"
        ),
        "oc_q_win_door": df["Question"].str.fullmatch("Windows and doors"),
        "oc_csi_three": df["csiMasterformat"] == 3,
        "oc_csi_four": df["csiMasterformat"] == 4,
        "oc_csi_five": df["csiMasterformat"] == 5,
        "oc_csi_six": df["csiMasterformat"] == 6,
        "oc_csi_seven": df["csiMasterformat"] == 7,
        "oc_csi_eight": df["csiMasterformat"] == 8,
        "oc_csi_nine": df["csiMasterformat"] == 9,
        "oc_csi_ten": df["csiMasterformat"] == 10,
        "oc_csi_twelve": df["csiMasterformat"] == 12,
        "oc_csi_twenty_two": df["csiMasterformat"] == 22,
        "oc_csi_twenty_three": df["csiMasterformat"] == 23,
        "oc_csi_twenty_five": df["csiMasterformat"] == 25,
        "oc_csi_twenty_six": df["csiMasterformat"] == 26,
        "oc_csi_thirty_one": df["csiMasterformat"] == 31,
        "oc_csi_thirty_three": df["csiMasterformat"] == 33,
        "oc_n_glass_sheath": df["Name"].str.contains("glass mat sheathing"),
        "oc_n_carpet": df["Name"].str.contains("carpet|Carpet|CARPET"),
        "oc_n_cladding": df["Name"].str.contains("cladding|Cladding|CLADDING"),
        "oc_n_flooring": df["Name"].str.contains("flooring|Flooring|FLOORING"),
        "oc_n_ceil_pan": df["Name"].str.contains("Ceiling Panels"),
        "oc_n_acoustic": df["Name"].str.contains("acoustic|Acoustic|ACOUSTIC"),
        "oc_n_deck": df["Name"].str.contains("deck|Deck|DECK"),
        "oc_n_timber": df["Name"].str.contains("timber|Timber|TIMBER"),
    }
    return filters


def create_all_tally_filters(df: pd.DataFrame) -> Dict[str, pd.Series]:
    """Creates a dictionary of Tally filters to be implemented.

    Args:
        df (pd.DataFrame): DataFrame of Tally entries

    Returns:
        Dict[str, pd.Series]: dictionary of Tally filters
    """
    filters = {
        "ty_clf_omni_na": pd.isna(df["CLF Omni"]),
        "rt_c_ceilings": df["Revit category"].str.fullmatch("Ceilings"),
        "rt_c_cw_panels": df["Revit category"].str.fullmatch(
            "Curtain Panels|Curtainwall Panels"
        ),
        "rt_c_cw_mull": df["Revit category"].str.fullmatch(
            "Curtain Wall Mullions|Curtainwall Mullions"
        ),
        "rt_c_door": df["Revit category"].str.fullmatch("Doors"),
        "rt_c_floor": df["Revit category"].str.fullmatch("Floors"),
        "rt_c_roof": df["Revit category"].str.fullmatch("Roofs"),
        "rt_c_railing": df["Revit category"].str.fullmatch("Railings"),
        "rt_c_stairs": df["Revit category"].str.fullmatch("Stairs"),
        "rt_c_str_col": df["Revit category"].str.fullmatch("Structural Columns"),
        "rt_c_str_con": df["Revit category"].str.fullmatch("Structural Connections"),
        "rt_c_str_fdn": df["Revit category"].str.fullmatch("Structural Foundations"),
        "rt_c_str_frm": df["Revit category"].str.fullmatch("Structural Framing"),
        "rt_c_wall": df["Revit category"].str.fullmatch("Walls"),
        "rt_c_window": df["Revit category"].str.fullmatch("Windows"),
        "rt_be_enc": df["Revit building element"].str.fullmatch("Enclosure"),
        "rt_be_int": df["Revit building element"].str.fullmatch("Interiors"),
        "rt_be_sub": df["Revit building element"].str.fullmatch("Substructure"),
        "rt_be_sup": df["Revit building element"].str.fullmatch("Superstructure"),
        "rt_fn_int": df["Revit family name"].str.contains(
            "int|Int|INT|interior|Interior|INTERIOR"
        ),
        "rt_fn_ext": df["Revit family name"].str.contains(
            "ext|Ext|EXT|exterior|Exterior|EXTERIOR"
        ),
        "rt_fn_rainscreen": df["Revit family name"].str.contains(
            "rainscreen|Rainscreen|RAINSCREEN"
        ),
        "rt_fn_enc": df["Revit family name"].str.contains(
            "enc|Enc|ENC|enclosure|Enclosure|ENCLOSURE"
        ),
        "rt_fn_shade": df["Revit family name"].str.contains(
            "shade|Shade|Shading|shading|SHADING"
        ),
        "rt_fn_glaze": df["Revit family name"].str.contains(
            "glazing|Glazing|GLAZING|glaze|Glaze|GLAZE"
        ),
        "rt_fn_fdn": df["Revit family name"].str.contains(
            "fdn|Fdn|FDN|foundation|Foundation|FOUNDATION"
        ),
        "rt_fn_ftg": df["Revit family name"].str.contains(
            "ftg|Ftg|FTG|footing|Footing|FOOTING"
        ),
        "rt_fn_below": df["Revit family name"].str.contains(
            "below|Below|BELOW|subgrade|Subgrade|SUBGRADE"
        ),
        "rt_fn_sog": df["Revit family name"].str.contains(
            "slab on grade|Slab on Grade|Slab On Grade|SLAB ON GRADE|sog|SOG"
        ),
        "rt_fn_grate": df["Revit family name"].str.contains(
            "grate|Grate|GRATE|grating|Grating|GRATING"
        ),
        "rt_fn_paver": df["Revit family name"].str.contains(
            "paver|Paver|PAVER|pavers|Pavers|PAVERS"
        ),
        "rt_fn_metal_deck": df["Revit family name"].str.contains(
            "metal deck|Metal deck|Metal Deck|METAL DECK"
        ),
        "rt_fn_parapet": df["Revit family name"].str.contains(
            "parapet|Parapet|PARAPET"
        ),
        "rt_fn_soffit": df["Revit family name"].str.contains("soffit|Soffit|SOFFIT"),
        "rt_fn_louver": df["Revit family name"].str.contains("louver|Louver|LOUVER"),
        "rt_fn_spandrel": df["Revit family name"].str.contains(
            "spandrel|Spandrel|SPANDREL"
        ),
        "rt_fn_partition": df["Revit family name"].str.contains(
            "partition|Partition|PARTITION"
        ),
        "rt_fn_bsmnt": df["Revit family name"].str.contains(
            "basement|Basement|BASEMENT"
        ),
        "rt_fn_retain": df["Revit family name"].str.contains(
            "retaining|Retaining|RETAINING"
        ),
        "rt_fn_stem": df["Revit family name"].str.contains("stem|Stem|STEM"),
        "rt_fn_cistern": df["Revit family name"].str.contains(
            "cistern|Cistern|CISTERN"
        ),
        "rt_fn_site": df["Revit family name"].str.contains("site|Site|SITE"),
        "rt_fn_battered": df["Revit family name"].str.contains(
            "battered|Battered|BATTERED"
        ),
        "rt_fn_caisson": df["Revit family name"].str.contains(
            "caisson|Caisson|CAISSON"
        ),
        "rt_fn_pile": df["Revit family name"].str.contains("pile|Pile|PILE"),
        "rt_fn_pier": df["Revit family name"].str.contains("pier|Pier|PIER"),
        "rt_fn_pit": df["Revit family name"].str.contains("pit|Pit|PIT"),
        "rt_fn_well": df["Revit family name"].str.contains("well|Well|WELL"),
        "rt_fn_fence": df["Revit family name"].str.contains("fence|Fence|FENCE"),
        "rt_fn_slab": df["Revit family name"].str.contains("slab|Slab|SLAB"),
        "rt_fn_pt": df["Revit family name"].str.contains(" PT "),
        "rt_fn_topping": df["Revit family name"].str.contains(
            "topping|Topping|TOPPING"
        ),
        "rt_fn_curb": df["Revit family name"].str.contains("curb|Curb|CURB"),
        "rt_fn_shaft": df["Revit family name"].str.contains("shaft|Shaft|SHAFT"),
        "rt_fn_shear": df["Revit family name"].str.contains("shear|Shear|SHEAR"),
        "rt_fn_ex": df["Revit family name"].str.match("ex|Ex|EX"),
        "rt_fn_p_naming": df["Revit family name"].str.match(
            "P-|P1|P2|P3|P4|P5|P6|P7|P8|P9"
        ),
        "rt_fn_wall_w": df["Revit family name"].str.match("W-|\\(W|\\(W-|W\\[|W[0-9]"),
        "ty_ed_09": df["Tally Entry Division"].str.fullmatch("09 - Finishes"),
        "ty_ed_08": df["Tally Entry Division"].str.fullmatch(
            "08 - Openings and Glazing"
        ),
        "ty_ed_07": df["Tally Entry Division"].str.fullmatch(
            "07 - Thermal and Moisture Protection"
        ),
        "ty_ed_06": df["Tally Entry Division"].str.fullmatch(
            "06 - Wood/Plastics/Composites"
        ),
        "ty_ed_05": df["Tally Entry Division"].str.fullmatch("05 - Metals"),
        "ty_ed_04": df["Tally Entry Division"].str.fullmatch("04 - Masonry"),
        "ty_ed_03": df["Tally Entry Division"].str.fullmatch("03 - Concrete"),
        "ty_ec_steel": df["Tally Entry Category"].str.fullmatch("Steel"),
        "ty_ec_alum": df["Tally Entry Category"].str.fullmatch("Aluminum"),
        "ty_ec_ceil_sys": df["Tally Entry Category"].str.fullmatch("Ceiling systems"),
        "ty_ec_cladding": df["Tally Entry Category"].str.fullmatch("Cladding"),
        "ty_en_cip_custom": df["Tally Entry Name"].str.fullmatch(
            "Cast-in-place concrete, custom mix|Cast-in-place concrete; custom mix"
        ),
        "ty_en_int": df["Tally Entry Name"].str.contains(
            "int|Int|INT|interior|Interior|INTERIOR"
        ),
        "ty_en_ext": df["Tally Entry Name"].str.contains(
            "ext|Ext|EXT|exterior|Exterior|EXTERIOR"
        ),
        "ty_en_toilet": df["Tally Entry Name"].str.contains("toilet|Toilet|TOILET"),
        "ty_en_igu": df["Tally Entry Name"].str.contains("IGU", regex=False),
        "ty_en_steel_sheet": df["Tally Entry Name"].str.match("Steel, sheet"),
        "ty_en_wood_framing": df["Tally Entry Name"].str.fullmatch("Wood framing"),
        "ty_en_part_board": df["Tally Entry Name"].str.fullmatch("Particle board"),
        "ty_en_ply_int": df["Tally Entry Name"].str.fullmatch(
            "Plywood, interior grade"
        ),
        "ty_en_mdf": df["Tally Entry Name"].str.fullmatch(
            "Medium density fiberboard \\(MDF\\)"
        ),
        "ty_en_ply_ext": df["Tally Entry Name"].str.fullmatch(
            "Plywood, exterior grade"
        ),
        "ty_en_ply_lvl": df["Tally Entry Name"].str.fullmatch(
            "Laminated veneer lumber \\(LVL\\)"
        ),
        "ty_en_ply_osb": df["Tally Entry Name"].str.fullmatch(
            "Oriented strandboard \\(OSB\\)"
        ),
        "ty_en_wood_framing_w_ins": df["Tally Entry Name"].str.fullmatch(
            "Wood framing with insulation"
        ),
        "ty_en_steel_plate": df["Tally Entry Name"].str.fullmatch("Steel, plate"),
        "ty_en_orn_wood": df["Tally Entry Name"].str.fullmatch("Ornamental wood"),
        "ty_en_fib_ins": df["Tally Entry Name"].str.fullmatch(
            "Fiberglass mat gypsum sheathing"
        ),
        "ty_mg_insulation": df["Material Group"].str.fullmatch("Insulation"),
        "ty_mg_coating": df["Material Group"].str.fullmatch("Coating"),
        "ty_mn_fib": df["Material Name"].str.fullmatch(
            "Fiberglass mat gypsum sheathing board"
        ),
    }
    return filters

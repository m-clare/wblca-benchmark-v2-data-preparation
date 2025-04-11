"""Creates dictionaries of filters for material quantity mapping."""

from typing import Dict
import pandas as pd
from wblca_benchmark_v2_data_prep.lca_results.enums import (
    MaterialQuantityOne,
    MaterialQuantityTwo,
)


def create_all_oneclick_filters(df: pd.DataFrame) -> Dict[str, pd.Series]:
    """Creates a dictionary of One Click filters to be implemented.

    Args:
        df (pd.DataFrame): DataFrame of One Click entries

    Returns:
        Dict[str, pd.Series]: dictionary of One Click filters
    """
    filters = {
        # concrete filters
        "conc_mq_one": df["MQ_1"].str.fullmatch(MaterialQuantityOne.CONCRETE.value),
        "ready_mix_other_mq_two": df["MQ_2"].str.fullmatch(
            MaterialQuantityTwo.READY_MIX_OTHER.value
        ),
        "conc_cat_mat_one": df["csiMasterformat"] == 3,
        "conc_cat_mat_two": df["Resource type"].str.fullmatch("Concrete"),
        "conc_slab_cat_mat_two": df["Resource type"].str.contains(
            "Concrete slabs (hollow and solid)", regex=False
        ),
        "ready_mix_cat_mat_two": df["Resource type"].str.contains("Ready-mix"),
        "aerated_conc_cat_mat_two": df["Resource type"].str.contains(
            "Aerated/Autoclaved concrete products", regex=False
        ),
        "cmu_cat_mat_two": df["Resource type"].str.contains("Concrete masonry unit"),
        "metal_cat_mat_two": df["Resource type"].str.fullmatch("Metal"),
        "conc_wall_ele_cat_mat_two": df["Resource type"].str.fullmatch(
            "Concrete wall elements"
        ),
        "str_conc_cat_mat_two": df["Resource type"].str.contains(
            "Structural concrete (beams, columns, piling)", regex=False
        ),
        "cement_cat_mat_two": df["Resource type"].str.contains("cement|Cement|CEMENT"),
        "conc_ad_mix_cat_mat_two": df["Resource type"].str.contains(
            "concrete admixture|Concrete admixture|Concrete Admixture"
        ),
        "lev_screed_cat_mat_three": df["Name"].str.contains(
            "Leveling screeds (for floors)", regex=False, na=False
        ),
        "lev_screed_cat_mat_two": df["Resource type"].str.contains(
            "Leveling screeds (for floors)", regex=False, na=False
        ),
        "other_precast_cat_mat_two": df["Resource type"].str.contains(
            "Other precast concrete products"
        ),
        "light_cat_mat_five": df["Resource"].str.contains("light|Light|LIGHT"),
        "weight_cat_mat_five": df["Resource"].str.contains("weight|Weight|WEIGHT"),
        "2500_psi_cat_mat_five": df["Resource"].str.contains(
            "0 - 2500|0-3000|concrete, 2500",
        ),
        "3000_psi_cat_mat_five": df["Resource"].str.contains(
            "2501|concrete, 3000",
        ),
        "4000_psi_cat_mat_five": df["Resource"].str.contains(
            "3001|concrete, 4000",
        ),
        "5000_psi_cat_mat_five": df["Resource"].str.contains(
            "4001|concrete, 5000",
        ),
        "6000_psi_cat_mat_five": df["Resource"].str.contains(
            "5001|concrete, 6000",
        ),
        "8000_psi_cat_mat_five": df["Resource"].str.contains(
            "6001|7000|concrete, 8000",
        ),
        "bcr_cat_mat_three": df["Name"].str.contains("bcr|Bcr|BCR"),
        "sand_cat_mat_three": df["Name"].str.contains("sand|Sand|SAND"),
        "cem_comp_cat_mat_three": df["Name"].str.contains(
            "cementitious components|Cementitious components|Cementitious Components"
        ),
        "water_for_cat_mat_three": df["Name"].str.contains(
            "water for|Water for|Water For"
        ),
        "aggregate_cat_mat_three": df["Name"].str.contains(
            "aggregate|Aggregate|AGGREGATE"
        ),
        "fibre_cement_prod_cat_mat_two": df["Resource type"].str.contains(
            "fibre cement products|Fibre cement products|Fibre Cement products"
        ),
        # steel filters
        "steel_mq_one": df["MQ_1"].str.fullmatch(MaterialQuantityOne.STEEL.value),
        "metals_cat_mat_one": df["csiMasterformat"] == 5,
        "alumi_cat_mat_two": df["Resource type"].str.contains("alumi|Alumi|ALUMI"),
        "fireproofing_cat_mat_two": df["Resource type"].str.contains(
            "fireproofing|Fireproofing|FIREPROOFING"
        ),
        "metal_coat_cat_mat_two": df["Resource type"].str.contains(
            "metal coating|Metal coating|Metal Coating"
        ),
        "sandwich_panel_cat_mat_two": df["Resource type"].str.contains(
            "Sandwich panels, metal"
        ),
        "ceiling_cat_mat_three": df["Name"].str.contains("ceiling|Ceiling|CEILING"),
        "cladding_cat_mat_three": df["Name"].str.contains("cladding|Cladding|CLADDING"),
        "roll_formed_cat_mat_three": df["Name"].str.contains(
            "roll formed|Roll formed|Roll Formed"
        ),
        "conc_reinf_cat_mat_two": df["Resource type"].str.contains(
            "Reinforcement for concrete (rebar)", regex=False
        ),
        "gen_reinf_cat_mat_three": df["Name"].str.contains(
            "Reinforcing|reinforcing|REINFORCING"
        ),
        "alumi_cat_mat_three": df["Name"].str.contains("alumi|Alumi|ALUMI"),
        "structural_cat_mat_three": df["Name"].str.contains(
            "structural|Structural|STRUCTURAL"
        ),
        "light_cat_mat_three": df["Name"].str.contains("light|Light|LIGHT"),
        "hollow_cat_mat_three": df["Name"].str.contains("hollow|Hollow|HOLLOW"),
        "plate_cat_mat_three": df["Name"].str.contains("plate|Plate|PLATE"),
        "cold_cat_mat_three": df["Name"].str.contains("cold|Cold|COLD"),
        "stud_cat_mat_five": df["Resource"].str.contains("stud|Stud|STUD"),
        "deck_cat_mat_five": df["Resource"].str.contains("deck|Deck|DECK"),
        "hss_cat_mat_five": df["Resource"].str.contains("hss|Hss|HSS"),
        "joist_cat_mat_three": df["Name"].str.contains("joist|Joist|JOIST"),
        # masonry filters
        "masonry_mq_one": df["MQ_1"].str.fullmatch(MaterialQuantityOne.MASONRY.value),
        "masonry_cat_mat_one": df["csiMasterformat"] == 4,
        "brick_cat_mat_two": df["Resource type"].str.fullmatch(
            "Brick, common clay brick"
        ),
        "stone_cat_mat_two": df["Resource type"].str.contains("stone|Stone|STONE"),
        "mortar_cat_mat_two": df["Resource type"].str.contains(
            "Mortar (masonry/bricklaying)", regex=False
        ),
        "cmu_h_cat_mat_three": df["Name"].str.contains(
            "Concrete masonry unit (CMU), hollow-core", regex=False
        ),
        "cmu_cat_mat_three": df["Name"].str.contains("Concrete masonry unit"),
        "stone_cladding_cat_mat_three": df["Name"].str.contains(
            "stone cladding|Stone cladding|Stone Cladding"
        ),
        "lw_conc_block_cat_mat_three": df["Name"].str.contains(
            "Lightweight concrete block"
        ),
        # aluminum filters
        "alumi_mq_one": df["MQ_1"].str.fullmatch(MaterialQuantityOne.ALUMINUM.value),
        "curtain_cat_mat_three": df["Name"].str.contains("curtain|Curtain|CURTAIN"),
        "door_cat_mat_two": df["Resource type"].str.contains("door|Door|DOOR"),
        "window_cat_mat_two": df["Resource type"].str.contains("window|Window|WINDOW"),
        "paint_cat_mat_two": df["Resource type"].str.contains(
            "paint|Paint|PAINT|paints|Paints|PAINTS"
        ),
        "partition_cat_mat_two": df["Resource type"].str.contains(
            "partition|partitioning|Partition|Partitioning|PIR"
        ),
        "storefront_cat_mat_three": df["Name"].str.contains(
            "storefront|Storefront|STOREFRONT"
        ),
        "composite_cat_mat_three": df["Name"].str.contains(
            "composite|Composite|COMPOSITE"
        ),
        "aluminum_window_cat_mat_three": df["Name"].str.contains(
            "aluminum window|Aluminum window|Aluminum Window"
        ),
        "frame_window_cat_mat_three": df["Name"].str.contains(
            "frame window|Frame window|Frame Window"
        ),
        "fixed_window_cat_mat_three": df["Name"].str.contains(
            "fixed window|Fixed window|Fixed Window"
        ),
        "casement_window_cat_mat_three": df["Name"].str.contains(
            "casement window|Casement window|Casement Window"
        ),
        "window_wall_cat_mat_three": df["Name"].str.contains(
            "window wall|Window wall|Window Wall"
        ),
        "framed_unitized_cat_mat_three": df["Name"].str.contains(
            "framed unitized|Framed unitized|Framed Unitized"
        ),
        "sandwich_cat_mat_three": df["Name"].str.contains("sandwich|Sandwich|SANDWICH"),
        "steel_cat_mat_three": df["Name"].str.contains("steel|Steel|STEEL"),
        "store_cat_mat_three": df["Name"].str.contains("store|Store|STORE"),
        "extru_cat_mat_three": df["Name"].str.contains("extru|Extru|EXTRU"),
        "sheet_cat_mat_three": df["Name"].str.contains("sheet|Sheet|SHEET"),
        "framing_cat_mat_three": df["Name"].str.contains("framing|Framing|FRAMING"),
        "framed_cat_mat_three": df["Name"].str.contains("framed|Framed|FRAMED"),
        # wood filters
        "wood_mq_one": df["MQ_1"].str.fullmatch(MaterialQuantityOne.WOOD.value),
        "wood_cat_mat_three": df["Name"].str.contains("wood|Wood|WOOD"),
        "lumber_cat_mat_three": df["Name"].str.contains("lumber|Lumber|LUMBER"),
        "timber_cat_mat_three": df["Name"].str.contains("timber|Timber|TIMBER"),
        "stud_cat_mat_three": df["Name"].str.contains("stud|Stud|STUD"),
        "osb_cat_mat_three": df["Name"].str.contains("OSB"),
        "lvl_cat_mat_three": df["Name"].str.contains("LVL"),
        "lsl_cat_mat_three": df["Name"].str.contains("LSL"),
        "clt_cat_mat_three": df["Name"].str.contains("CLT"),
        "glue_cat_mat_three": df["Name"].str.contains("glue|Glue|GLUE"),
        "mdf_cat_mat_three": df["Name"].str.contains(
            "MDF|medium density fiberboard|Medium density fiberboard"
        ),
        "fiberboard_mdf_cat_mat_two": df["Resource type"].str.contains(
            "Fiberboard (MDF)", regex=False
        ),
        "particleboard_cat_mat_three": df["Name"].str.contains(
            "particleboard|Particleboard|particle board|Particle board"
        ),
        "textile_cat_mat_two": df["Resource type"].str.contains(
            "textile|Textile|TEXTILE"
        ),
        "plastic_cat_mat_two": df["Resource type"].str.contains(
            "plastic|Plastic|PLASTIC"
        ),
        "furniture_cat_mat_two": df["Resource type"].str.contains(
            "furniture|Furniture|FURNITURE"
        ),
        "softwood_cat_mat_three": df["Name"].str.contains("softwood|Softwood|SOFTWOOD"),
        "plywood_cat_mat_three": df["Name"].str.contains("plywood|Plywood|PLYWOOD"),
        "hardwood_cat_mat_three": df["Name"].str.contains("hardwood|Hardwood|HARDWOOD"),
        # glazing filters
        "glazing_mq_one": df["MQ_1"].str.fullmatch(MaterialQuantityOne.GLAZING.value),
        "glazing_cat_mat_one": df["csiMasterformat"] == 8,
        "glass_pane_cat_mat_two": df["Resource type"].str.contains(
            "glass pane|Glass pane|Glass Pane"
        ),
        "glazing_cat_mat_two": df["Resource type"].str.contains(
            "glazing|Glazing|GLAZING"
        ),
        "igu_cat_mat_three": df["Name"].str.contains("IGU"),
        # insulation filters
        "insulation_mq_one": df["MQ_1"].str.fullmatch(
            MaterialQuantityOne.INSULATION.value
        ),
        "insulation_cat_mat_two": df["Resource type"].str.contains(
            "insulation|Insulation|INSULATION", na=False
        ),
        "acoustic_insul_panel_cat_mat_two": df["Resource type"].str.contains(
            "acoustic insulation panel|Acoustic insulation panel|Acoustic Insulation panel"
        ),
        "xps_cat_mat_three": df["Name"].str.contains("XPS"),
        "pir_cat_mat_three": df["Name"].str.contains("PIR"),
        "batt_cat_mat_three": df["Name"].str.contains("batt|Batt|BATT"),
        "min_wool_cat_mat_three": df["Name"].str.contains(
            "mineral wool|Mineral wool|Mineral Wool"
        ),
        "rock_wool_cat_mat_three": df["Name"].str.contains(
            "rock wool|Rock wool|Rock Wool"
        ),
        "stone_wool_cat_mat_three": df["Name"].str.contains(
            "stone wool|Stone wool|Stone Wool"
        ),
        "mineral_fiber_cat_mat_three": df["Name"].str.contains(
            "mineral fiber|Mineral fiber|Mineral Fiber"
        ),
        "cellulose_cat_mat_three": df["Name"].str.contains("Cellulose"),
        "eps_cat_mat_three": df["Name"].str.contains("EPS"),
        "spray_cat_mat_three": df["Name"].str.contains("spray|Spray|SPRAY"),
        "foam_cat_mat_three": df["Name"].str.contains("foam|Foam|FOAM"),
        # gypsum filters
        "gypsum_mq_one": df["MQ_1"].str.fullmatch(
            MaterialQuantityOne.GYPSUM.value, na=False
        ),
        "gypsum_cat_mat_two": df["Resource type"].str.contains(
            "gypsum|Gypsum|GYPSUM", na=False
        ),
        "gypsum_board_cat_mat_two": df["Resource type"].str.contains(
            "gypsum board|Gypsum board|Gypsum Board", na=False
        ),
        "acoustic_ceiling_panel_cat_mat_three": df["Name"].str.contains(
            "acoustic ceiling|Acoustic ceiling|Acoustic Ceiling"
        ),
        "glass_cat_mat_three": df["Name"].str.contains("glass|Glass|GLASS", na=False),
        "ceiling_panel_cat_mat_six": df["Datasource"].str.contains(
            "ceiling panel|Ceiling panel|Ceiling Panel"
        ),
        # roofing and waterproofing filters
        "roofing_mq_one": df["MQ_1"].str.fullmatch(MaterialQuantityOne.ROOF.value),
        "roof_cat_mat_three": df["Name"].str.contains(" roof | Roof | ROOF "),
        "roof_start_cat_mat_three": df["Name"].str.match("roof|Roof|ROOF"),
        "roofing_cat_mat_three": df["Name"].str.contains(
            " roofing | Roofing | ROOFING "
        ),
        "roofing_start_cat_mat_three": df["Name"].str.match("roofing|Roofing|ROOFING"),
        "plas_mem_cat_mat_two": df["Resource type"].str.contains(
            "plastic membrane|Plastic membrane|Plastic Membrane"
        ),
        "bitumen_cat_mat_two": df["Resource type"].str.contains(
            "Bitumen and other roofing"
        ),
        "bitumen_cat_mat_three": df["Name"].str.contains("bitumen|Bitumen|BITUMEN"),
        "sbs_cat_mat_three": df["Name"].str.contains("SBS"),
        "tpo_cat_mat_three": df["Name"].str.contains("TPO"),
        "epdm_cat_mat_three": df["Name"].str.contains("EPDM"),
        "pvc_cat_mat_three": df["Name"].str.contains("PVC"),
        "HDPE_cat_mat_three": df["Name"].str.contains("HDPE"),
        "green_roof_cat_mat_three": df["Name"].str.contains(
            "green roof|Green roof|Green Roof"
        ),
        "asphalt_cat_mat_three": df["Name"].str.contains("asphalt|Asphalt|ASPHALT"),
        "shingle_cat_mat_three": df["Name"].str.contains("shingle|Shingle|SHINGLE"),
        # fireproofing filters
        "fireproof_mq_one": df["MQ_1"].str.fullmatch(
            MaterialQuantityOne.FIREPROOF.value
        ),
        "fireproof_cat_mat_two": df["Resource type"].str.contains(
            "fireproofing|Fireproofing|FIREPROOFING", na=False
        ),
        "fire_resistive_cat_mat_three": df["Name"].str.contains(
            "Spray-applied fire-resistive", regex=False
        ),
        "cementitious_cat_mat_three": df["Name"].str.contains(
            "cementitious|Cementitious|CEMENTITIOUS",
        ),
        "intumescent_cat_mat_three": df["Name"].str.contains(
            "intumescent|Intumescent|INTUMESCENT",
        ),
        "spray_applied_cat_mat_three": df["Name"].str.contains(
            "spray-applied|Spray-applied|Spray-Applied", regex=False
        ),
        # door filters
        "door_mq_one": df["MQ_1"].str.fullmatch(MaterialQuantityOne.DOOR_FRAME.value),
        "door_cat_mat_three": df["Name"].str.contains("door|Door|DOOR"),
        "industrial_door_cat_mat_two": df["Resource type"].str.contains(
            "Metal and industrial doors",
        ),
        "frame_cat_mat_three": df["Name"].str.contains("frame|Frame|FRAME"),
        "alum_framed_glass_door_cat_mat_two": df["Resource type"].str.contains(
            "Aluminium-framed glass doors", regex=False
        ),
        "alum_frame_window_cat_mat_two": df["Resource type"].str.contains(
            "aluminium frame window|Aluminium frame window",
        ),
        "sliding_cat_mat_three": df["Name"].str.contains("sliding|Sliding|SLIDING"),
        "revolving_cat_mat_three": df["Name"].str.contains(
            "revolving|Revolving|REVOLVING"
        ),
        "fiberglass_cat_mat_three": df["Name"].str.contains(
            "fiberglass|Fiberglass|FIBERGLASS"
        ),
        "particle_cat_mat_three": df["Name"].str.contains("particle|Particle|PARTICLE"),
        # window filters
        "window_mq_one": df["MQ_1"].str.fullmatch(
            MaterialQuantityOne.WINDOW_FRAME.value
        ),
        "window_cat_mat_three": df["Name"].str.contains("window|Window|WINDOW"),
        "part_sys_cat_mat_two": df["Resource type"].str.contains(
            "Partitioning systems (without windows)", regex=False
        ),
        "pvc_frame_window_cat_mat_two": df["Resource type"].str.contains(
            "PVC frame windows"
        ),
        "glass_fac_cat_mat_two": df["Resource type"].str.contains(
            "Glass facades and glazing"
        ),
        "aluminium_cat_mat_two": df["Resource type"].str.contains(
            "aluminium|Aluminium|ALUMINIUM",
        ),
        "unitized_cat_mat_three": df["Name"].str.contains("unitized|Unitized|UNITIZED"),
        # acoustic ceiling filters
        "acous_ceilings_mq_one": df["MQ_1"].str.fullmatch(
            MaterialQuantityOne.ACOUSTIC_CEILINGS.value
        ),
        "metal_ceiling_cat_mat_three": df["Name"].str.contains(
            "metal ceiling|Metal ceiling|Metal Ceiling"
        ),
        "suspen_cat_mat_three": df["Name"].str.contains("suspen|Suspen|SUSPEN"),
        "fiber_cat_mat_three": df["Name"].str.contains("fiber|Fiber|FIBER"),
        # cladding filters
        "cladding_mq_one": df["MQ_1"].str.fullmatch(MaterialQuantityOne.CLADDING.value),
        "formed_cat_mat_three": df["Name"].str.contains("formed|Formed|FORMED"),
        "roll_formed_start_cat_mat_three": df["Name"].str.match(
            "roll formed|Roll formed|Roll Formed"
        ),
        "sandwich_panel_cat_mat_three": df["Name"].str.contains(
            "sandwich panel|Sandwich panel|Sandwich Panel"
        ),
        "insulated_metal_cat_mat_three": df["Name"].str.contains(
            "insulated metal|Insulated metal|Insulated Metal"
        ),
        "fibre_cement_prod_cat_mat_three": df["Name"].str.contains(
            "fibre cement products|Fibre cement products|Fibre Cement products"
        ),
        "fibre_cement_board_cat_mat_three": df["Name"].str.contains(
            "fibre cement board|Fibre cement board|Fibre Cement board"
        ),
        "fiber_reinf_cat_mat_three": df["Name"].str.contains(
            "fiber reinforced|Fiber reinforced|Fiber Reinforced"
        ),
        "stucco_cat_mat_three": df["Name"].str.contains("sutcco|Stucco|STUCCO"),
        "polyethylene_cat_mat_three": df["Name"].str.contains(
            "polyethylene|Polyethylene|POLYETHYLENE"
        ),
        "high_pressure_cat_mat_three": df["Name"].str.contains(
            "high pressure|High pressure|High Pressure"
        ),
        "hpl_cat_mat_three": df["Name"].str.contains("HPL"),
        # adhesive seal filters
        "adhes_seal_mq_one": df["MQ_1"].str.fullmatch(
            MaterialQuantityOne.ADHES_SEAL.value
        ),
        # air and vapor barrier filters
        "vapor_barrier_mq_one": df["MQ_1"].str.fullmatch(
            MaterialQuantityOne.AIR_VAPOR.value
        ),
        "sealants_cat_mat_two": df["Resource type"].str.contains(
            "Sealants (silicone and others)", regex=False
        ),
        # coatings filters
        "coatings_mq_one": df["MQ_1"].str.fullmatch(MaterialQuantityOne.COATINGS.value),
        "paint_cat_mat_three": df["Name"].str.contains("paint|Paint|PAINT"),
        "coating_cat_mat_two": df["Resource type"].str.contains(
            "coating|Coating|COATING"
        ),
        "paint_coat_laq_cat_mat_two": df["Resource type"].str.fullmatch(
            "Paints, coatings and lacquers"
        ),
        "high_perform_coating_cat_mat_three": df["Name"].str.contains(
            "high performance coating|High performance coating"
        ),
        # flooring and tile filters
        "floor_tile_mq_one": df["MQ_1"].str.fullmatch(MaterialQuantityOne.FLOOR.value),
        "res_floor_cat_mat_two": df["Resource type"].str.contains(
            "resilient flooring|Resilient flooring"
        ),
        "lam_floor_cat_mat_two": df["Resource type"].str.contains(
            "laminate flooring|Laminate flooring"
        ),
        "lin_floor_cat_mat_two": df["Resource type"].str.contains(
            "linoleum flooring|Linoleum flooring"
        ),
        "wall_floor_tile_cat_mat_two": df["Resource type"].str.contains(
            "Wall and floor tiles"
        ),
        "other_floor_cat_mat_two": df["Resource type"].str.contains(
            "Other flooring types"
        ),
        "vinyl_cat_mat_three": df["Name"].str.contains(
            "vinyl|Vinyl|VINYL",
        ),
        "rubber_cat_mat_three": df["Name"].str.contains(
            "rubber|Rubber|RUBBER",
        ),
        "carpet_cat_mat_three": df["Name"].str.contains(
            "carpet|Carpet|CARPET",
        ),
        "terrazzo_cat_mat_three": df["Name"].str.contains(
            "terrazzo|Terrazzo|TERRAZZO",
        ),
        "ceramic_cat_mat_two": df["Resource type"].str.contains(
            "ceramic|Ceramic|CERAMIC",
        ),
        "porcelain_cat_mat_two": df["Resource type"].str.contains(
            "porcelain|Porcelain|PORCELAIN",
        ),
        "carpet_flooring_cat_mat_two": df["Resource type"].str.contains(
            "carpet flooring|Carpet flooring|Carpet Flooring"
        ),
        "raised_access_floor_cat_mat_three": df["Name"].str.contains(
            "raised access floor system|Raised access floor system"
        ),
        # synthetic composites filters
        "synth_comp_mq_one": df["MQ_1"].str.fullmatch(
            MaterialQuantityOne.SYNTH_COMP.value
        ),
        "plas_profile_cat_mat_two": df["Resource type"].str.contains(
            "Plastic profiles and products"
        ),
        # wall coverings filters
        "wall_coverings_mq_one": df["MQ_1"].str.fullmatch(
            MaterialQuantityOne.WALL_COVERINGS.value
        ),
        "vinyl_cover_cat_mat_three": df["Name"].str.contains(
            "vinyl wallcovering|Vinyl wallcovering|Vinyl Wallcovering"
        ),
        # other filters
        "other_mq_one": df["MQ_1"].str.fullmatch(MaterialQuantityOne.OTHER.value),
        "other_mq_two": df["MQ_2"].str.fullmatch(MaterialQuantityTwo.OTHER.value),
        # misc csiMasterformat filters
        "oc_csi_six": df["csiMasterformat"] == 6,
        "oc_csi_seven": df["csiMasterformat"] == 7,
        "oc_csi_nine": df["csiMasterformat"] == 9,
        "oc_csi_ten": df["csiMasterformat"] == 10,
        "oc_csi_twelve": df["csiMasterformat"] == 12,
        "oc_csi_twenty_two": df["csiMasterformat"] == 22,
        "oc_csi_twenty_three": df["csiMasterformat"] == 23,
        "oc_csi_twenty_five": df["csiMasterformat"] == 25,
        "oc_csi_twenty_six": df["csiMasterformat"] == 26,
        "oc_csi_thirty_one": df["csiMasterformat"] == 31,
        "oc_csi_thirty_three": df["csiMasterformat"] == 33,
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
        # concrete filters
        "conc_mq_one": df["MQ_1"].str.fullmatch(MaterialQuantityOne.CONCRETE.value),
        "conc_cat_mat_one": df["Tally Entry Division"].str.fullmatch("03 - Concrete"),
        "conc_cat_mat_two": df["Material Group"].str.fullmatch("Concrete"),
        "cip_cat_ele_four": df["Tally Entry Category"].str.fullmatch(
            "Cast-in-place Concrete"
        ),
        "cip_lw_3000_cat_mat_four": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete, lightweight structural concrete, 3000 psi"
        ),
        "cip_lw_3000_cat_mat_four_alt1": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete, lightweight structural concrete, 2501-3000 psi"
        ),
        "cip_lw_3000_cat_mat_four_alt2": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete; lightweight structural concrete; 2501-3000 psi"
        ),
        "cip_lw_4000_cat_mat_four": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete, lightweight structural concrete, 4000 psi"
        ),
        "cip_lw_4000_cat_mat_four_alt1": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete, lightweight structural concrete, 3001-4000 psi"
        ),
        "cip_lw_4000_cat_mat_four_alt2": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete; lightweight structural concrete; 3001-4000 psi"
        ),
        "cip_lw_5000_cat_mat_four": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete, lightweight structural concrete, 5000 psi"
        ),
        "cip_lw_5000_cat_mat_four_alt1": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete, lightweight structural concrete, 4001-5000 psi"
        ),
        "cip_lw_5000_cat_mat_four_alt2": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete; lightweight structural concrete; 4001-5000 psi"
        ),
        "cip_nw_2500_cat_mat_four": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete, structural concrete, 2500 psi"
        ),
        "cip_nw_2500_cat_mat_four_alt1": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete, structural concrete, 0-2500 psi"
        ),
        "cip_nw_2500_cat_mat_four_alt2": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete; structural concrete; 0-2500 psi"
        ),
        "cip_nw_3000_cat_mat_four": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete, structural concrete, 3000 psi"
        ),
        "cip_nw_3000_cat_mat_four_alt1": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete, structural concrete, 2501-3000 psi"
        ),
        "cip_nw_3000_cat_mat_four_alt2": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete; structural concrete; 2501-3000 psi"
        ),
        "cip_nw_4000_cat_mat_four": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete, structural concrete, 4000 psi"
        ),
        "cip_nw_4000_cat_mat_four_alt1": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete, structural concrete, 3001-4000 psi"
        ),
        "cip_nw_4000_cat_mat_four_alt2": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete; structural concrete; 3001-4000 psi"
        ),
        "cip_nw_5000_cat_mat_four": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete, structural concrete, 5000 psi"
        ),
        "cip_nw_5000_cat_mat_four_alt1": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete, structural concrete, 4001-5000 psi"
        ),
        "cip_nw_5000_cat_mat_four_alt2": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete; structural concrete; 4001-5000 psi"
        ),
        "cip_nw_6000_cat_mat_four": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete, structural concrete, 6000 psi"
        ),
        "cip_nw_6000_cat_mat_four_alt1": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete, structural concrete, 5001-6000 psi"
        ),
        "cip_nw_6000_cat_mat_four_alt2": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete; structural concrete; 5001-6000 psi"
        ),
        "cip_nw_8000_cat_mat_four": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete, structural concrete, 8000 psi"
        ),
        "cip_nw_8000_cat_mat_four_alt1": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete, structural concrete, 6001-8000 psi"
        ),
        "cip_nw_8000_cat_mat_four_alt2": df["Tally Entry Name"].str.contains(
            "Cast-in-place concrete; structural concrete; 6001-8000 psi"
        ),
        "precast_cat_ele_four": df["Tally Entry Category"].str.fullmatch(
            "Precast Concrete"
        ),
        "gfrc_cat_mat_three": df["Material Name"].str.contains("gfrc|Gfrc|GFRC"),
        "self_lvl_under_cat_mat_three": df["Material Name"].str.contains(
            "self-leveling underlayment|Self-leveling underlayment|Self-leveling Underlayment",
        ),
        "str_conc_cat_mat_three": df["Material Name"].str.contains(
            "structural concrete|Structural concrete|Structural concrete",
        ),
        "lw_conc_cat_mat_three": df["Material Name"].str.contains(
            "lightweight concrete|Lightweight concrete|Lightweight Concrete",
        ),
        # steel filters
        "steel_mq_one": df["MQ_1"].str.fullmatch(MaterialQuantityOne.STEEL.value),
        "metals_cat_mat_one": df["Tally Entry Division"].str.fullmatch("05 - Metals"),
        "metal_cat_mat_two": df["Material Group"].str.fullmatch("Metal"),
        "steel_cat_ele_four": df["Tally Entry Category"].str.fullmatch("Steel"),
        "steel_cat_mat_four": df["Tally Entry Name"].str.contains("steel|Steel|STEEL"),
        "stair_cat_ele_four": df["Tally Entry Category"].str.fullmatch("Stair"),
        "reinf_cat_ele_four": df["Tally Entry Category"].str.fullmatch(
            "Concrete Reinforcement", na=False
        ),
        "gal_steel_support_cat_mat_three": df["Material Name"].str.fullmatch(
            "Galvanized steel support", na=False
        ),
        "chromium_cat_mat_three": df["Material Name"].str.contains(
            "chromium|Chromium|CHROMIUM"
        ),
        "reinf_rod_cat_mat_three": df["Material Name"].str.contains(
            "Steel, reinforcing rod|Steel; reinforcing rod"
        ),
        "reinf_cmc_cat_mat_three": df["Material Name"].str.contains(
            "Steel, concrete reinforcing steel, CMC - EPD"
        ),
        "alt_reinf_cmc_cat_mat_three": df["Material Name"].str.contains(
            "Steel; concrete reinforcing steel; CMC - EPD"
        ),
        "reinf_csri_cat_mat_three": df["Material Name"].str.contains(
            "Steel, fabricated steel reinforcement, CRSI - EPD"
        ),
        "alt_reinf_csri_cat_mat_three": df["Material Name"].str.contains(
            "Steel; fabricated steel reinforcement; CRSI - EPD"
        ),
        "reinf_weld_w_cat_mat_three": df["Material Name"].str.contains(
            "Steel, welded wire mesh|Steel; welded wire mesh"
        ),
        "reinf_woven_w_cat_mat_three": df["Material Name"].str.contains(
            "Steel, woven wire mesh|Steel; woven wire mesh"
        ),
        "hot_rolled_cat_mat_five": df["Tally Entry Description"].str.contains(
            "Hot rolled|Hot-rolled"
        ),
        "hot_rolled_cat_mat_three": df["Material Name"].str.contains(
            "Hot rolled|Hot-rolled"
        ),
        "cold_formed_cat_mat_five": df["Tally Entry Description"].str.contains(
            "cold formed|cold-formed|Cold formed|Cold-formed"
        ),
        "hss_cat_mat_four": df["Tally Entry Name"].str.contains(
            "HSS section|rectangular tubing|round tubing"
        ),
        "plate_cat_mat_four": df["Tally Entry Name"].str.contains("plate|Plate|PLATE"),
        "w_cat_mat_four": df["Tally Entry Name"].str.contains("W section"),
        "stud_cat_mat_four": df["Tally Entry Name"].str.contains("stud|Stud|STUD"),
        "deck_cat_mat_four": df["Tally Entry Name"].str.contains("deck|Deck|DECK"),
        "steel_cable_cat_mat_three": df["Material Name"].str.fullmatch("Steel, cable"),
        "pr_conc_bm_cat_mat_four": df["Tally Entry Name"].str.fullmatch(
            "Precast concrete beam"
        ),
        "quarter_in_cat_mat_five": df["Tally Entry Description"].str.contains(
            "1/4", regex=False
        ),
        "joist_cat_mat_three": df["Material Name"].str.contains("joist|Joist|JOIST"),
        # masonry filters
        "masonry_mq_one": df["MQ_1"].str.fullmatch(MaterialQuantityOne.MASONRY.value),
        "masonry_cat_mat_one": df["Tally Entry Division"].str.fullmatch("04 - Masonry"),
        "masonry_cat_mat_two": df["Material Group"].str.fullmatch("Masonry"),
        "stone_cat_mat_two": df["Material Group"].str.fullmatch("Stone", na=False),
        "mortar_cat_mat_three": df["Material Name"].str.contains(
            "Mortar|mortar|MORTAR"
        ),
        "cmu_cat_ele_four": df["Tally Entry Category"].str.fullmatch("CMU"),
        "brick_cat_ele_four": df["Tally Entry Category"].str.fullmatch("Brick"),
        "stone_cat_ele_four": df["Tally Entry Category"].str.fullmatch("Stone"),
        "grout_cat_mat_three": df["Material Name"].str.contains("grout|Grout|GROUT"),
        # aluminum filters
        "alum_mq_one": df["MQ_1"].str.fullmatch(MaterialQuantityOne.ALUMINUM.value),
        "aluminum_cat_mat_three": df["Material Name"].str.contains(
            "aluminum|Aluminum|ALUMINUM"
        ),
        "aluminum_cat_mat_four": df["Tally Entry Name"].str.contains(
            "aluminum|Aluminum|ALUMINUM"
        ),
        "alum_faced_comp_cat_mat_three": df["Material Name"].str.contains(
            "Aluminum-faced composite|Aluminum-Faced composite|Alumnium-Faced Composite"
        ),
        "ins_metal_cat_mat_four": df["Tally Entry Name"].str.contains(
            "insulated metal|Insulated metal|Insulated Metal"
        ),
        "metal_wall_cat_mat_four": df["Tally Entry Name"].str.contains(
            "metal wall|Metal wall|Metal Wall"
        ),
        "ceil_sys_cat_ele_four": df["Tally Entry Category"].str.contains(
            "ceiling system|Ceiling system|Ceiling System"
        ),
        "door_cat_ele_four": df["Tally Entry Category"].str.contains(
            "door|Door|DOOR", na=False
        ),
        "door_cat_mat_three": df["Material Name"].str.contains("door|Door|DOOR"),
        "mullion_cat_ele_four": df["Tally Entry Category"].str.contains(
            "mullion|Mullion|MULLION"
        ),
        "window_frame_cat_ele_four": df["Tally Entry Category"].str.contains(
            "window frame|Window frame|Window Frame"
        ),
        "extru_cat_mat_three": df["Material Name"].str.contains("extru|Extru|EXTRU"),
        "sheet_cat_mat_three": df["Material Name"].str.contains("sheet|Sheet|SHEET"),
        "formed_cat_mat_three": df["Material Name"].str.contains(
            "formed|Formed|FORMED"
        ),
        "siding_cat_mat_three": df["Material Name"].str.contains(
            "siding|Siding|SIDING"
        ),
        "alum_mull_sys_cat_mat_five": df["Tally Entry Description"].str.contains(
            "Aluminum mullion framing|Aluminum Mullion framing|Aluminum Mullion Framing",
            na=False,
        ),
        # wood filters
        "wood_mq_one": df["MQ_1"].str.fullmatch(MaterialQuantityOne.WOOD.value),
        "wood_cat_mat_two": df["Material Group"].str.contains("wood|Wood|WOOD"),
        "soft_cat_mat_three": df["Material Name"].str.contains("soft|Soft|SOFT"),
        "plywood_cat_mat_three": df["Material Name"].str.contains(
            "plywood|Plywood|PLYWOOD"
        ),
        "osb_cat_mat_three": df["Material Name"].str.contains("OSB"),
        "mdf_cat_mat_three": df["Material Name"].str.contains("MDF"),
        "psl_cat_mat_three": df["Material Name"].str.contains("PSL"),
        "glulam_cat_mat_three": df["Material Name"].str.contains(
            "glulam|Glulam|GLULAM"
        ),
        "clt_cat_mat_three": df["Material Name"].str.contains("CLT"),
        "i_joist_cat_mat_three": df["Material Name"].str.contains(
            "i-joist|I-joist|I-Joist"
        ),
        "lsl_cat_mat_three": df["Material Name"].str.contains("LSL"),
        "lvl_cat_mat_three": df["Material Name"].str.contains("LVL"),
        "hardwood_cat_mat_three": df["Material Name"].str.contains(
            "hardwood|Hardwood|HARDWOOD"
        ),
        "lumber_cat_mat_three": df["Material Name"].str.contains(
            "lumber|Lumber|LUMBER"
        ),
        "heavy_cat_mat_three": df["Material Name"].str.contains("heavy|Heavy|HEAVY"),
        # glazing filters
        "glazing_mq_one": df["MQ_1"].str.fullmatch(MaterialQuantityOne.GLAZING.value),
        "glazing_cat_mat_two": df["Material Group"].str.contains(
            "glazing|Glazing|GLAZING"
        ),
        "spandrel_cat_mat_two": df["Material Group"].str.contains(
            "spandrel|Spandrel|SPANDREL"
        ),
        "igu_cat_mat_four": df["Tally Entry Name"].str.contains("IGU"),
        "glass_cat_mat_three": df["Material Name"].str.contains("glass|Glass|GLASS"),
        # insulation filters
        "insulation_mq_one": df["MQ_1"].str.fullmatch(
            MaterialQuantityOne.INSULATION.value
        ),
        "insulation_cat_mat_two": df["Material Group"].str.contains(
            "insulation|Insulation|INSULATION"
        ),
        "gyp_board_cat_mat_four": df["Tally Entry Name"].str.contains(
            "Wall board, gypsum|Wall board; gypsum"
        ),
        "xps_cat_mat_three": df["Material Name"].str.contains("XPS"),
        "pir_cat_mat_three": df["Material Name"].str.contains("PIR"),
        "min_wool_cat_mat_three": df["Material Name"].str.contains(
            "mineral wool|Mineral wool|Mineral Wool"
        ),
        "fiberglass_cat_mat_three": df["Material Name"].str.contains(
            "fiberglass|Fiberglass|FIBERGLASS"
        ),
        "glass_fiber_cat_mat_three": df["Material Name"].str.contains(
            "glass fiber|Glass fiber|Glass Fiber"
        ),
        "glass_wool_cat_mat_three": df["Material Name"].str.contains(
            "glass wool|Glass wool|Glass Wool"
        ),
        "cellulose_cat_mat_three": df["Material Name"].str.contains("Cellulose"),
        "eps_cat_mat_three": df["Material Name"].str.contains("EPS"),
        "spray_cat_mat_three": df["Material Name"].str.contains("Spray"),
        "board_cat_mat_four": df["Tally Entry Name"].str.contains("board|Board|BOARD"),
        "low_cat_mat_three": df["Material Name"].str.contains("low|Low|LOW"),
        "high_cat_mat_three": df["Material Name"].str.contains("high|High|HIGH"),
        "ecose_cat_mat_three": df["Material Name"].str.contains("ECOSE"),
        "ddp_cat_mat_three": df["Material Name"].str.contains("DDP"),
        "115_cat_mat_three": df["Material Name"].str.contains("115"),
        "132_cat_mat_three": df["Material Name"].str.contains("132"),
        "135_cat_mat_three": df["Material Name"].str.contains("135"),
        "140_cat_mat_three": df["Material Name"].str.contains("140"),
        "432_cat_mat_three": df["Material Name"].str.contains("432"),
        # gypsum filters
        "gypsum_mq_one": df["MQ_1"].str.fullmatch(MaterialQuantityOne.GYPSUM.value),
        "plaster_cat_mat_two": df["Material Group"].str.contains(
            "plaster|Plaster|PLASTER"
        ),
        "foil_facing_cat_mat_three": df["Material Name"].str.fullmatch("Foil facing"),
        "fib_glass_cat_mat_three": df["Material Name"].str.fullmatch(
            "Fiberglass mat gypsum sheathing board"
        ),
        # roofing filters
        "roofing_mq_one": df["MQ_1"].str.fullmatch(MaterialQuantityOne.ROOF.value),
        "roof_mem_cat_mat_two": df["Material Group"].str.contains(
            "Roofing membrane|Roofing Membrane|Roof membrane|Roof Membrane"
        ),
        "roof_cat_mat_three": df["Material Name"].str.contains(" roof | Roof | ROOF "),
        "roof_start_cat_mat_three": df["Material Name"].str.match("roof|Roof|ROOF"),
        "roofing_cat_mat_three": df["Material Name"].str.contains(
            " roofing | Roofing | ROOFING "
        ),
        "roofing_start_cat_mat_three": df["Material Name"].str.match(
            "roofing|Roofing|ROOFING"
        ),
        "roof_cat_mat_four": df["Tally Entry Name"].str.contains(
            " roof | Roof | ROOF "
        ),
        "roof_start_cat_mat_four": df["Tally Entry Name"].str.match("roof|Roof|ROOF"),
        "insul_cat_mat_four": df["Tally Entry Name"].str.contains("insul|Insul|INSUL"),
        "sbs_cat_mat_three": df["Material Name"].str.contains("SBS"),
        "mod_bitumen_cat_mat_three": df["Material Name"].str.contains(
            "modified bitumen|Modified bitumen|Modified Bitumen"
        ),
        "built_up_cat_mat_three": df["Material Name"].str.contains(
            "built-up|Built-up|Built-Up"
        ),
        "bur_cat_mat_three": df["Material Name"].str.contains("BUR"),
        "tpo_cat_mat_three": df["Material Name"].str.contains("TPO"),
        "epdm_cat_mat_three": df["Material Name"].str.contains("EPDM"),
        "PVC_cat_mat_three": df["Material Name"].str.contains("PVC"),
        # fireproofing filters
        "fireproof_mq_one": df["MQ_1"].str.fullmatch(
            MaterialQuantityOne.FIREPROOF.value
        ),
        "fireproof_cat_mat_two": df["Material Group"].str.contains(
            "fireproofing|Fireproofing|FIREPROOFING", na=False
        ),
        "cementitious_cat_mat_three": df["Material Name"].str.contains(
            "cementitious|Cementitious|CEMENTITIOUS"
        ),
        "intumescent_cat_mat_three": df["Material Name"].str.contains(
            "intumescent|Intumescent|INTUMESCENT"
        ),
        # doors and frames filters
        "doors_and_frames_mq_one": df["MQ_1"].str.fullmatch(
            MaterialQuantityOne.DOOR_FRAME.value
        ),
        "door_cat_mat_two": df["Material Group"].str.contains("door|Door|DOOR"),
        "door_frame_cat_mat_two": df["Material Group"].str.contains(
            "door frame|Door frame|Door Frame"
        ),
        "wood_cat_mat_three": df["Material Name"].str.contains("wood|Wood|WOOD"),
        "steel_cat_mat_three": df["Material Name"].str.contains("steel|Steel|STEEL"),
        "galvanized_cat_mat_three": df["Material Name"].str.contains(
            "galvanized|Galvanized|GALVANIZED"
        ),
        "hollow_cat_mat_three": df["Material Name"].str.contains(
            "hollow|Hollow|HOLLOW"
        ),
        "opening_hardware_cat_mat_two": df["Material Group"].str.contains(
            "opening hardware|Opening hardware|Opening Hardware"
        ),
        # window frames filters
        "window_frame_mq_one": df["MQ_1"].str.fullmatch(
            MaterialQuantityOne.WINDOW_FRAME.value
        ),
        "window_frame_cat_mat_two": df["Material Group"].str.contains(
            "window frame|Window frame|Window Frame"
        ),
        "aluminum_cat_mat_five": df["Tally Entry Description"].str.contains(
            "aluminum|Aluminum|ALUMINUM"
        ),
        # acoustic ceilings filters
        "acous_ceilings_mq_one": df["MQ_1"].str.fullmatch(
            MaterialQuantityOne.ACOUSTIC_CEILINGS.value
        ),
        "ceil_tile_cat_mat_two": df["Material Group"].str.contains(
            "ceiling tile|Ceiling tile|Ceiling Tile"
        ),
        "ceil_tile_cat_mat_three": df["Material Name"].str.contains(
            "ceiling tile|Ceiling tile|Ceiling Tile"
        ),
        "fiber_cat_mat_three": df["Material Name"].str.contains("fiber|Fiber|FIBER"),
        "suspended_cat_mat_three": df["Material Name"].str.contains(
            "suspended|Suspended|SUSPENDED"
        ),
        # synthetic composite filters
        "synth_comp_mq_one": df["MQ_1"].str.fullmatch(
            MaterialQuantityOne.SYNTH_COMP.value
        ),
        "composite_cat_mat_two": df["Material Group"].str.contains(
            "composite|Composite|COMPOSITE"
        ),
        "plastic_cat_mat_two": df["Material Group"].str.contains(
            "plastic|Plastic|PLASTIC"
        ),
        # cladding filters
        "cladding_mq_one": df["MQ_1"].str.fullmatch(MaterialQuantityOne.CLADDING.value),
        "cladding_cat_mat_two": df["Material Group"].str.contains(
            "cladding|Cladding|CLADDING"
        ),
        "terracotta_cat_mat_three": df["Material Name"].str.contains(
            "terracotta|Terracotta|TERRACOTTA"
        ),
        "fastener_cat_mat_three": df["Material Name"].str.contains(
            "fastener|Fastener|FASTENER"
        ),
        "stucco_cat_mat_three": df["Material Name"].str.contains(
            "stucco|Stucco|STUCCO"
        ),
        "copper_cat_mat_three": df["Material Name"].str.contains(
            "copper|Copper|COPPER"
        ),
        "zinc_cat_mat_three": df["Material Name"].str.contains("zinc|Zinc|ZINC"),
        "fiber_cem_cat_mat_three": df["Material Name"].str.contains(
            "fiber cement|Fiber cement|Fiber Cement"
        ),
        "gfrc_cat_mat_four": df["Tally Entry Name"].str.contains("gfrc|Gfrc|GFRC"),
        "panel_cat_mat_four": df["Tally Entry Name"].str.contains("panel|Panel|PANEL"),
        "metal_roofing_cat_mat_four": df["Tally Entry Name"].str.contains(
            "metal roofing|Metal roofing|Metal Roofing"
        ),
        "siding_cat_mat_four": df["Tally Entry Name"].str.contains(
            "siding|Siding|SIDING"
        ),
        "insulated_cat_mat_three": df["Material Name"].str.contains(
            "insulated|Insulated|INSULATED"
        ),
        # adhesive and sealants filters
        "adhes_seal_mq_one": df["MQ_1"].str.fullmatch(
            MaterialQuantityOne.ADHES_SEAL.value
        ),
        "adhesive_cat_mat_two": df["Material Group"].str.contains(
            "adhesive|Adhesive|ADHESIVE",
        ),
        "sealant_cat_mat_two": df["Material Group"].str.contains(
            "sealant|Sealant|SEALANT",
        ),
        # air and vapor barriers filters
        "vapor_barrier_mq_one": df["MQ_1"].str.fullmatch(
            MaterialQuantityOne.AIR_VAPOR.value
        ),
        "vapor_barrier_cat_mat_two": df["Material Group"].str.contains(
            "vapor barrier|Vapor barrier|Vapor Barrier",
        ),
        # coatings filters
        "coatings_mq_one": df["MQ_1"].str.fullmatch(MaterialQuantityOne.COATINGS.value),
        "coating_cat_mat_two": df["Material Group"].str.contains(
            "coating|Coating|COATING",
        ),
        "metal_coating_cat_mat_two": df["Material Group"].str.contains(
            "metal coating|Metal coating|Metal Coating",
        ),
        "paint_cat_mat_three": df["Material Name"].str.contains("paint|Paint|PAINT"),
        # flooring and tile filters
        "floor_tile_mq_one": df["MQ_1"].str.fullmatch(MaterialQuantityOne.FLOOR.value),
        "floor_tile_cat_mat_two": df["Material Group"].str.contains(
            "Flooring & Tile",
            regex=False,
        ),
        "trim_rubber_cat_mat_three": df["Material Name"].str.contains(
            "Trim, rubber",
        ),
        "carpet_cat_mat_three": df["Material Name"].str.contains(
            "carpet|Carpet|CARPET"
        ),
        "ceramic_cat_mat_three": df["Material Name"].str.contains(
            "ceramic|Ceramic|CERAMIC"
        ),
        "porcelain_cat_mat_three": df["Material Name"].str.contains(
            "porcelain|Porcelain|PORCELAIN"
        ),
        "stone_tile_cat_mat_four": df["Tally Entry Name"].str.contains(
            "stone tile|Stone tile|Stone Tile"
        ),
        "vinyl_cat_mat_three": df["Material Name"].str.contains("vinyl|Vinyl|VINYL"),
        "rubber_cat_mat_three": df["Material Name"].str.contains(
            "rubber|Rubber|RUBBER"
        ),
        # other metals filters
        "other_metals_mq_one": df["MQ_1"].str.fullmatch(
            MaterialQuantityOne.OTH_METALS.value
        ),
        "brass_cat_mat_three": df["Material Name"].str.contains("brass|Brass|BRASS"),
        "bronze_cat_mat_three": df["Material Name"].str.contains(
            "bronze|Bronze|BRONZE"
        ),
        "titanium_cat_mat_three": df["Material Name"].str.contains(
            "titanium|Titanium|TITANIUM"
        ),
        # wall coverings filters
        "wall_coverings_mq_one": df["MQ_1"].str.fullmatch(
            MaterialQuantityOne.WALL_COVERINGS.value
        ),
        "wall_cover_cat_mat_two": df["Material Group"].str.contains(
            "wall coverings|Wall coverings|Wall Coverings",
        ),
        # other filters
        "other_mq_one": df["MQ_1"].str.fullmatch(MaterialQuantityOne.OTHER.value),
        "other_mq_two": df["MQ_2"].str.fullmatch(MaterialQuantityTwo.OTHER.value),
    }
    return filters

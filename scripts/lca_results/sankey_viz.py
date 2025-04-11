"""Creates sankey flow diagrams for material mapping."""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sankeyflow import Sankey
from wblca_benchmark_v2_data_prep.lca_results.enums import MaterialQuantityOne


def create_sankey_per_material():
    """Create a sankey diagram per material in the dataset and
    show its different material makeups.
    """
    current_file_path = Path(__file__)
    main_directory = current_file_path.parents[2]
    combined_tally_path = main_directory.joinpath(
        "data/lca_results/harmonized/tally_harmonized.csv"
    )
    combined_oneclick_path = main_directory.joinpath(
        "data/lca_results/harmonized/oneclick_harmonized.csv"
    )

    dfs_dict = {
        "tally": pd.read_csv(combined_tally_path),
        "oneclick": pd.read_csv(combined_oneclick_path),
    }

    material_to_check_list = [str(mat.value) for mat in MaterialQuantityOne]

    for df_type, df_to_check in dfs_dict.items():
        figure_directory = main_directory.joinpath(f"figures/sankey/{df_type}")

        for material_to_check in material_to_check_list:
            if df_to_check[df_to_check["MQ_1"] == material_to_check].empty:
                continue

            nodes, flows = create_sankey_flows_and_nodes(
                material_to_check=material_to_check, df_to_check=df_to_check
            )

            create_sankey_diagram(
                flows=flows,
                nodes=nodes,
                figure_dictionary=figure_directory,
                material_to_check_name=material_to_check,
            )


def create_sankey_diagram(
    flows: list[tuple],
    nodes: list[tuple],
    figure_dictionary: Path,
    material_to_check_name: str,
) -> None:
    """Create sankey diagram and save to figure_dictionary location.

    Args:
        flows (list[tuple]): List of flows for Sankey Diagram
        nodes (list[tuple]): List of nodes for Sankey Diagram
        figure_dictionary (Path): directory location for images
    """
    plt.figure(figsize=(35, 20), dpi=144)
    plt.rcParams["font.family"] = "Lucida Sans"
    s = Sankey(
        flows=flows,
        nodes=nodes,
        flow_color_mode="source",
        node_pad_y_min=0.015,
    )
    for node_list in s.nodes:
        for node in node_list:
            node.label_opts = {"fontsize": 14}
    s.draw()
    plt.subplots_adjust(
        left=0.1, right=0.9, top=0.95, bottom=0.05
    )  # Adjust values as needed
    plt.savefig(figure_dictionary.joinpath(f"{material_to_check_name}.png"))
    plt.close()


def create_sankey_flows_and_nodes(
    material_to_check: str, df_to_check: pd.DataFrame
) -> tuple[list, list]:
    """Create the sankey flows and nodes.

    Args:
        material_to_check_list (list[str]): List of materials to check
        df_to_check (pd.DataFrame): DataFrame to work on

    Returns:
        tuple[str, str]: nodes for sankey and flows for sankey
    """

    mat_to_check_df = df_to_check[df_to_check["MQ_1"] == material_to_check]

    mat_to_check_mq_two_unique_names = sorted(mat_to_check_df["MQ_2"].unique().tolist())
    mq_2_names_nodes = []
    mq_2_names_flows = []
    mq_2_material_nodes = []

    for mq_2_name in mat_to_check_mq_two_unique_names:
        if mq_2_name == material_to_check:
            temp_mq_two_name = f"{mq_2_name}_material"
        else:
            temp_mq_two_name = mq_2_name
        mq_2_name_df = mat_to_check_df[mat_to_check_df["MQ_2"] == mq_2_name]
        mq_2_names_unique_mat_names = sorted(
            mq_2_name_df["Cat_Mat_3"].unique().tolist()
        )

        length_of_mq_2_name_df = len(mq_2_name_df)
        tuple_for_mq_2_name_nodes = (
            temp_mq_two_name,
            length_of_mq_2_name_df,
            {"color": "#8DC6E8"},
        )

        tuple_for_mq_2_name_flows = (
            material_to_check,
            temp_mq_two_name,
            length_of_mq_2_name_df,
        )
        mq_2_names_nodes.append(tuple_for_mq_2_name_nodes)
        mq_2_names_flows.append(tuple_for_mq_2_name_flows)

        for unique_mq_two_mat_name in mq_2_names_unique_mat_names:
            if unique_mq_two_mat_name == material_to_check or mq_2_name:
                temp_unique_mq_two_mat_name = f"{unique_mq_two_mat_name}_material"
            else:
                temp_unique_mq_two_mat_name = unique_mq_two_mat_name
            unique_mq_two_mat_name_df = mq_2_name_df[
                mq_2_name_df["Cat_Mat_3"] == unique_mq_two_mat_name
            ]
            length_of_mq_2_name_material_df = len(unique_mq_two_mat_name_df)
            tuple_for_mq_2_material_nodes = (
                temp_unique_mq_two_mat_name,
                length_of_mq_2_name_material_df,
                {"color": "#6E6F72"},
            )

            tuple_for_mq_2_material_flows = (
                temp_mq_two_name,
                temp_unique_mq_two_mat_name,
                length_of_mq_2_name_material_df,
            )
            mq_2_material_nodes.append(tuple_for_mq_2_material_nodes)
            mq_2_names_flows.append(tuple_for_mq_2_material_flows)

    level_one_nodes = [(material_to_check, len(mat_to_check_df), {"color": "#FFB71B"})]
    final_nodes = [level_one_nodes, mq_2_names_nodes, mq_2_material_nodes]
    flows = mq_2_names_flows

    return final_nodes, flows


if __name__ == "__main__":
    create_sankey_per_material()

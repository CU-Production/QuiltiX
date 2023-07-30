import os

from QuiltiX import constants
from tests import helpers


def load_amd_wooden_flooring_mtlx():
    with helpers.quiltix_instance() as editor:
        mx_file = os.path.join(
            constants.ROOT,
            "src",
            "QuiltiX",
            "resources",
            "materials",
            "Wooden_Flooring_004_1k_8b",
            "Wooden_Flooring_SHDR.mtlx",
        )
        # TODO: why do we not have to assign the material here?
        editor.qx_node_graph.load_graph_from_mx_file(mx_file)


if __name__ == "__main__":
    load_amd_wooden_flooring_mtlx()

import functools
import graphviz as gv
import os

graph = functools.partial(gv.Graph, format='svg')
digraph = functools.partial(gv.Digraph, format='svg')


def draw(tf_node, session, filename="layer_output"):
    """

    :param tf_node:
        rv of session.graph.get_tensor_by_name('node_name'))
    """
    allnodes = set([tf_node.name])
    allconnections = set([])
    nodes_to_traverse = set([tf_node.name])

    new_nodes_to_traverse = set([])
    while nodes_to_traverse:
        del new_nodes_to_traverse
        new_nodes_to_traverse = set([])

        for node_to_name in nodes_to_traverse:
            node = session.graph.get_tensor_by_name(node_to_name)
            input_nodenames = [i.name for i in node.op.inputs]
            allnodes.update(input_nodenames)

            for node_from_name in input_nodenames:
                allconnections.add((node_from_name, node_to_name))

            new_nodes_to_traverse.update(input_nodenames)

        del nodes_to_traverse
        nodes_to_traverse = new_nodes_to_traverse

    mapping = {}
    graph = digraph()

    for i, node_name in enumerate(allnodes):
        mapping[node_name] = "{}".format(i)
        graph.node(mapping[node_name], label=node_name)

    for c_f, c_t in allconnections:
        graph.edge(mapping[c_f], mapping[c_t])

    graph.render(os.path.join(os.path.expandvars("$HOME"), filename))


from data_types.graphs import Graph

def contract_edge(edge, graph: Graph):
    """
    This is the edge contraction step. It basically takes an edge (u, v) and merges the vertices (into something like uv)
    that form the edge's endpoints. All other edges strictly between u and v are removed, 
    and all edges going out of an coming into u and v will now go out of/come into contracted vertex uv

    It might be important to note that we can make this significantly faster by modifying our implementation of the graph.

    ---
    O(|V| + |E|)
    """

    u = edge[0]
    v = edge[1]
    combined = str(u) + str(v)
    graph.replace_vertex(u, combined)
    graph.replace_vertex(v, combined)

    # Now we want to remove any and all self-loops
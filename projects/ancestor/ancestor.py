
def earliest_ancestor(ancestors, starting_node):
    # Build the graph
    graph = Graph()

    for parent, child in ancestors:
    if parent not in graph.vertices:
        graph.add_vertex(parent)
    if child not in graph.vertices:
        graph.add_vertex(child)
    # Build in reverse order
    graph.add_edge(child, parent)

    # Do a BFS
    
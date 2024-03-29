import networkx as nx
from calculate_graph_nx import (
    calculate_clustering_coefficient, 
    calculate_graph_degree,
    calculate_graph_density,
    calculate_graph_diameter)
from degree_distribution import degree_distribution_plot


# Create an empty graph
graph = nx.Graph()

edge_file = 'aves-wildbird-network.edges'
with open(edge_file, 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Ommiting blank lines
        if line.strip():
            # Split the line into source and target nodes
            source, target, weight, _ = line.strip().split()
            weight = float(weight)
            # Add the edge to the graph
            graph.add_edge(source, target, weight=weight)


if __name__ == '__main__':
    print("Number of nodes:", graph.number_of_nodes())
    print("Number of edges:", graph.number_of_edges())
    # print("Graph nodes:", graph.nodes())
    calculate_graph_degree(graph)
    calculate_graph_density(graph)
    calculate_graph_diameter(graph)
    calculate_clustering_coefficient(graph)
    degree_distribution_plot(graph)






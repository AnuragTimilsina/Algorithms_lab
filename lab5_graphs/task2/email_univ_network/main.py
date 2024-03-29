import networkx as nx
from calculate_graph_nx import (
    calculate_clustering_coefficient, 
    calculate_graph_degree,
    calculate_graph_density,
    calculate_graph_diameter)
from degree_distribution import degree_distribution_plot


# Create an empty graph
graph = nx.Graph()

edge_file = 'email-univ.edges'
with open(edge_file, 'r') as file:
    # Iterate over each line in the file
    for line in file:
        if line.split():
            # Split the line into source and target nodes
            source, target = line.strip().split()
            # Add the edge to the graph
            graph.add_edge(source, target)


if __name__ == '__main__':
    print("Number of nodes:", graph.number_of_nodes())
    print("Number of edges:", graph.number_of_edges())
    # print("Graph nodes:", graph.nodes())
    calculate_graph_degree(graph)
    calculate_graph_density(graph)
    calculate_graph_diameter(graph)
    calculate_clustering_coefficient(graph)
    degree_distribution_plot(graph)





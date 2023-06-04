import networkx as nx
from task2.graph1.calculate_graph_nx import (
    calculate_clustering_coefficient, 
    calculate_graph_degree,
    calculate_graph_density,
    calculate_graph_diameter)


# Create an empty graph
graph = nx.Graph()

edge_file = 'aves-barn-swallow-contact-network.edges'
with open(edge_file, 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Split the line into source and target nodes
        source, target, weight = line.strip().split()
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

    # Verifying the clustering coefficient from the library. 
    clustering_coeffs = nx.clustering(graph)

    # Calculate the average clustering coefficient
    total_coeffs = sum(clustering_coeffs.values())
    num_nodes = graph.number_of_nodes()

    if num_nodes > 0:
        avg_clustering_coeff = total_coeffs / num_nodes
    else:
        avg_clustering_coeff = 0

    print("Average Clustering Coefficient (Library):", avg_clustering_coeff)






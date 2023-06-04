import networkx as nx


def calculate_graph_degree(graph):
    # Calculate the average degree
    degrees = [degree for node, degree in graph.degree()]
    average_degree = sum(degrees) / len(degrees)

    print("Average degree:", average_degree)


def calculate_graph_density(graph):
    # Calculate the density
    num_edges = graph.number_of_edges()
    num_nodes = graph.number_of_nodes()

    if num_nodes > 1:
        density = (2 * num_edges) / (num_nodes * (num_nodes - 1))
    else:
        density = 0

    print("Density:", density)


def calculate_graph_diameter(graph):
    # Calculate the diameter
    diameter = nx.diameter(graph)

    print("Diameter:", diameter)


def calculate_clustering_coefficient(graph):
    # Calculate the clustering coefficient for each node
    clustering_coeffs = {}
    for node in graph.nodes():
        neighbors = list(graph.neighbors(node))
        num_neighbors = len(neighbors)
        
        if num_neighbors > 1:
            num_connections = 0
            
            # Count the number of connections between neighbors
            for i in range(num_neighbors - 1):
                for j in range(i + 1, num_neighbors):
                    if graph.has_edge(neighbors[i], neighbors[j]):
                        num_connections += 1
            
            # Calculate the clustering coefficient for the node
            clustering_coeffs[node] = (2 * num_connections) / (num_neighbors * (num_neighbors - 1))
        else:
            clustering_coeffs[node] = 0

    # Calculate the average clustering coefficient
    num_nodes = graph.number_of_nodes()
    if num_nodes > 0:
        avg_clustering_coeff = sum(clustering_coeffs.values()) / num_nodes
    else:
        avg_clustering_coeff = 0

    print("Average Clustering Coefficient (Scratch):", avg_clustering_coeff)


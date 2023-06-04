import networkx as nx
import matplotlib.pyplot as plt


def plot_graph(graph):
    # Draw the graph
    pos = nx.spring_layout(graph)  # Define the node positions
    labels = nx.get_edge_attributes(graph, 'weight')  # Get the edge weights as labels

    nx.draw_networkx(graph, pos=pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=labels)

    plt.title("Weighted Graph")
    plt.axis("off")
    plt.show()
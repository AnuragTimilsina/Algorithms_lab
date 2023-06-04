import matplotlib.pyplot as plt


def degree_distribution_plot(graph):
    # Get the degree of each node
    degrees = dict(graph.degree())

    # Count the number of nodes with each degree
    degree_distribution = {}
    for degree in degrees.values():
        if degree in degree_distribution:
            degree_distribution[degree] += 1
        else:
            degree_distribution[degree] = 1

    # Normalize the degree distribution (optional)
    total_nodes = graph.number_of_nodes()
    for degree in degree_distribution:
        degree_distribution[degree] /= total_nodes

    # Print the degree distribution
    for degree, count in degree_distribution.items():
        print(f"Degree {degree}: {count}")

    # Plot the degree distribution
    plt.bar(degree_distribution.keys(), degree_distribution.values())
    plt.xlabel('Degree')
    plt.ylabel('Frequency')
    plt.title('Degree Distribution')
    plt.show()

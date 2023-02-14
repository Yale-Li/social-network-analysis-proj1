import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def plot_degree_dist(G):
    # array of degree for each node in the node list
    degrees = [G.degree(node) for node in G.nodes()]
    plt.hist(degrees)
    plt.xlabel('degree')
    plt.ylabel('Number of Nodes with the given degree')
    plt.title('Degree Distribution')
    plt.show()
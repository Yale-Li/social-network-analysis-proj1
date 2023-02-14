import networkx as nx
import matplotlib.pyplot as plt


def plot_constructed_graph(G):
    # nodelabels = nx.get_node_attributes(G, "name")
    # nx.draw_networkx_labels(G, pos, labels = nodelabels)
    nx.draw(G, with_labels=False)
    
    # plotting the constructed graph
    plt.show()

import networkx as nx
import matplotlib.pyplot as plt
def plotClosenessCentrality(G):
    dict = nx.closeness_centrality(G)

    lst = [round(v, 5) for v in dict.values()]
    plt.hist(lst)
    plt.show()

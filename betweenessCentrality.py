import networkx as nx
import matplotlib.pyplot as plt


def computeAndPlotBetweenessCentrality(G):
    # compute centrality
    centrality = nx.betweenness_centrality(G, k=10, endpoints=True)

    # compute community structure
    lpc = nx.community.label_propagation_communities(G)
    community_index = {n: i for i, com in enumerate(lpc) for n in com}

    #### draw graph ####
    fig, ax = plt.subplots(figsize=(20, 15))
    pos = nx.spring_layout(G, k=0.15, seed=4572321)
    node_color = [community_index[n] for n in G]
    node_size = [v * 20000 for v in centrality.values()]

    nx.draw_networkx(
        G,
        pos=pos,
        with_labels=False,
        node_color=node_color,
        node_size=node_size,
        edge_color="gainsboro",
        alpha=0.4,
    )

    # Title/legend
    font = {"color": "k", "fontweight": "bold", "fontsize": 20}
    ax.set_title("Gene functional association network (C. elegans)", font)
    # Change font color for legend
    font["color"] = "r"

    ax.text(
        0.80,
        0.10,
        "node color = community structure",
        horizontalalignment="center",
        transform=ax.transAxes,
        fontdict=font,
    )

    ax.text(
        0.80,
        0.06,
        "node size = betweenness centrality",
        horizontalalignment="center",
        transform=ax.transAxes,
        fontdict=font,
    )

    # Resize figure for label readability
    ax.margins(0.1, 0.05)
    fig.tight_layout()
    plt.axis("off")
    plt.show()

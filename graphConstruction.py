import networkx as nx
import matplotlib.pyplot as plt
import csv

import degreeDistribution
import plottingConstructedGraph
import betweenessCentrality

# constants declaration
userId = 0
name = 1
userName = 2
idIndex = 0
followingIndex = 1


G = nx.Graph()
G.graph["Name"] = "Twitter Relationship Graph"

with open("users.csv", 'r', errors='ignore') as usersFile:
    csvreader = csv.reader(usersFile)
    next(csvreader)
    for row in csvreader:
        G.add_nodes_from(
            [(row[userId], {"name": row[name], "userName": row[userName]})])

usersFile.close()

pos = nx.spring_layout(G)

with open("relationship.csv", 'r') as relationshipsFile:
    csvreader = csv.reader(relationshipsFile)
    next(csvreader)
    for row in csvreader:
        G.add_edge(row[idIndex], row[followingIndex])


print("enter choice of operation")
print(" Enter 1 - for plotting the constructed graph\n")
print(" Enter 2 - for plotting degree distribution histogram\n")
print(" Enter 3 - for computing and plotting betweeness centrality\n")
print(" Enter 4 - for computing and plotting closeness centrality\n")

choice = int(input())

match choice:
    case 1:
        # plotting the graph
        plottingConstructedGraph.plot_constructed_graph(G)
    case 2:
        # plot degree distribution
        degreeDistribution.plot_degree_dist(G)
    case 3:
        # compute and plot Betweeness Centrality
        betweenessCentrality.computeAndPlotBetweenessCentrality(G)

    case _:
        print("wrong input feeded")
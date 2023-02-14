import networkx as nx
import matplotlib.pyplot as plt
import csv

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
        G.add_nodes_from([(row[userId], {"name": row[name], "userName": row[userName]})])

usersFile.close()

pos = nx.spring_layout(G);

with open("relationship.csv", 'r') as relationshipsFile:
    csvreader = csv.reader(relationshipsFile)
    next(csvreader)
    for row in csvreader:
        G.add_edge(row[idIndex], row[followingIndex])

nx.draw(G, with_labels=False)
# nodelabels = nx.get_node_attributes(G, "name")
# nx.draw_networkx_labels(G, pos, labels = nodelabels)

plt.show()

dict = nx.closeness_centrality(G)

lst = [round(v, 5) for v in dict.values()]
plt.hist(lst)
plt.show()
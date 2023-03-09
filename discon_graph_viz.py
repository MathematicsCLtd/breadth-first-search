import networkx as nx
import matplotlib.pyplot as plt

graph = {
    0: {1, 2},
    1: {0},
    2: {0},
    3: {4},
    4: {3}
}

# create a graph object
G = nx.Graph(graph)

# draw the graph
nx.draw(G, with_labels=True)

# display the graph
plt.show()

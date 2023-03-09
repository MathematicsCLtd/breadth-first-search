import networkx as nx
import matplotlib.pyplot as plt

graph = {
    0: {1, 2},
    1: {0, 3, 4},
    2: {0},
    3: {1},
    4: {1, 5},
    5: {4}
}

# create a graph object
G = nx.Graph(graph)

# draw the graph
nx.draw(G, with_labels=True)

# display the graph
plt.show()

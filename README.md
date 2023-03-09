# Breadth-first search (BFS)

A common brute-force algorithm that works well for a small number of nodes.

## Implementation

This algorithm takes in a graph and returns a set of all visited vertices. It uses a deque to keep track of the vertices to visit and a set to keep track of the visited vertices. The graph parameter should be a dictionary where the keys are the vertices and the values are sets of adjacent vertices.

## Testing
* The first test case tests a disconnected graph where the BFS algorithm should visit all vertices.
* The second test case tests a graph with a single node where the BFS algorithm should only visit that node.
* The third test case tests a regular graph where the BFS algorithm should visit all vertices reachable from the starting vertex.

## Visualizations
Run locally to see the graphs used in the first and third test cases.

## Use Cases
* Shortest Path Finding: BFS is often used to find the shortest path between two vertices in a graph. For example, BFS can be used to find the shortest path between two locations on a map, where the vertices represent locations and the edges represent roads or paths connecting them.
* Web Crawling: BFS is used in web crawling algorithms to discover and index web pages. The algorithm starts from a given web page and explores its neighboring pages, then moves on to explore the neighbors of the neighbors, and so on. This helps search engines like Google to find and index all the web pages on the internet.
* Social Network Analysis: BFS can be used to analyze social networks such as Facebook, Twitter, and LinkedIn. In a social network, vertices represent users, and edges represent relationships between users (such as friendships or following relationships). BFS can be used to explore a user's network of friends or followers, and to find the shortest path between two users in the network.
* Game AI: BFS can be used in game AI to search for the best move in a game. For example, in a chess game, BFS can be used to search for the best move by exploring all possible moves from the current position and all possible responses from the opponent.
* Network Routing: BFS can be used in network routing algorithms to find the shortest path between two nodes in a network. For example, BFS can be used to find the shortest path between two computers in a network or the shortest path between two cities in a transportation network.

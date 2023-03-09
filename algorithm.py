from collections import deque

def bfs(graph):
    """
    Perform a breadth-first search (BFS) traversal of a graph.
    
    Parameters:
    graph (dict): A dictionary where the keys are vertices and the values are sets of adjacent vertices.
    
    Returns:
    set: A set of all visited vertices in the graph.
    
    Notes:
    This function can handle disconnected graphs, graphs with a single node, and regular graphs.
    """
    visited = set()
    queue = deque()
    for vertex in graph:
        if vertex not in visited:
            queue.append(vertex)
            while queue:
                vertex = queue.popleft()
                if vertex not in visited:
                    visited.add(vertex)
                    queue.extend(graph[vertex] - visited)
    return visited


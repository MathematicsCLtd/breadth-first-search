import algorithm    # The code to test

def test_bfs_disconnected_graph():
    graph = {
        0: {1, 2},
        1: {0},
        2: {0},
        3: {4},
        4: {3}
    }
    assert algorithm.bfs(graph) == {0, 1, 2, 3, 4}

def test_bfs_single_node():
    graph = {
        0: set()
    }
    assert algorithm.bfs(graph) == {0}

def test_bfs_regular_graph():
    graph = {
        0: {1, 2},
        1: {0, 3, 4},
        2: {0},
        3: {1},
        4: {1, 5},
        5: {4}
    }
    assert algorithm.bfs(graph) == {0, 1, 2, 3, 4, 5}
    assert algorithm.bfs(graph) == {1, 0, 3, 4, 2, 5}
    assert algorithm.bfs(graph) == {4, 1, 5, 0, 3, 2}

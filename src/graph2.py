"""Docstring for graph traversal."""

from graph import Graph
from time import time

def depth_first_traversal(g, start_val):
    """Perform a full depth-first traversal of the

    graph beginning at start_val. Return the full
    visited path when traversal is complete.
    """
    visited, stack = [], [start_val]
    while stack:
        path = stack.pop(0)
        visited.append(path)
        n = []
        for child in g.neighbors(path):
            if child not in visited:
                n.append(child)
        n += stack
        stack = n
    return visited


def breadth_first_traversal(g, start_val):
    """Perform a full breath-first traversal of the

    graph beginning at start_val. Return the full
    visited path when traversal is complete.
    """
    visited, stack = [], [start_val]
    while stack:
        path = stack.pop(0)
        if path not in visited:
            visited.append(path)
            stack.extend(g.neighbors(path))
    return visited


def is_cycle_dfs(g, start_val):
    """Perform depth-first traversal of graph

    beginning at start_val to detect if graph has a cycle.
    """
    found = False
    visited, stack = [], [start_val]
    while stack:
        path = stack.pop(0)
        visited.append(path)
        n = []
        for child in g.neighbors(path):
            if any(x in visited for x in g.neighbors(child)):
                found = True
                return found
            if child not in visited:
                n.append(child)
        n += stack
        stack = n
    return found


def is_cycle_bfs(g, start_val):
    """Perform a breath-first traversal of graph

    beginning at start_val to detect if graph has a cycle.
    """
    found = False
    visited, stack = [], [start_val]
    while stack:
        path = stack.pop(0)
        if path not in visited:
            visited.append(path)
            stack.extend(g.neighbors(path))
            if any(x in visited for x in g.neighbors(path)):
                found = True
                return found
    return found


def time_dfs(g, start_val):
    """Time depth search performance."""
    t0 = time()
    depth_first_traversal(g, start_val)
    t1 = time()
    return 'depth search time for 10 edges: ' + str(round(t1 - t0, 5)) + " sec."


def time_bfs(g, start_val):
    """Time breadth search performance."""
    t0 = time()
    breadth_first_traversal(g, start_val)
    t1 = time()
    return 'breath search time for 10 edges: ' + str(round(t1 - t0, 5)) + " sec."


if __name__ == '__main__':
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    g.add_edge('C', 'G')
    g.add_edge('D', 'H')
    g.add_edge('D', 'I')
    g.add_edge('E', 'J')
    g.add_edge('E', 'K')
    g.add_edge('E', 'A')
    print('depth: ', depth_first_traversal(g, 'A'))
    print('breadth: ', breadth_first_traversal(g, 'A'))
    print(time_bfs(g, 'A'))
    print(time_dfs(g, 'A'))

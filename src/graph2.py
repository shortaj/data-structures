"""Docstring for graph traversal."""

from graph import Graph


def depth_first_traversal(g, start_val):
    """Perform a full depth-first traversal of the

    graph beginning at start_val. Return the full
    visited path when traversal is complete."""
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
    visited path when traversal is complete."""
    visited, stack = [], [start_val]
    while stack:
        path = stack.pop(0)
        if path not in visited:
            visited.append(path)
            stack.extend(g.neighbors(path))
    return visited

"""Module for testing graph2.py."""
import pytest
from graph import Graph

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


def test_depth_first_traversal():
    """Perform depth first traversal of g."""
    from graph import Graph
    from graph2 import depth_first_traversal
    assert depth_first_traversal(g, 'A') == ['A', 'B', 'D', 'H', 'I', 'E', 'J', 'K', 'C', 'F', 'G']


def test_breadth_first_traversal():
    """Perform breadth first traversal of g."""
    from graph import Graph
    from graph2 import breadth_first_traversal
    assert breadth_first_traversal(g, 'A') == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']


def test_is_cycle_dft():
    """Perform if graph has a cycle with depth first traversal."""
    from graph import Graph
    from graph2 import is_cycle_dfs
    assert is_cycle_dfs(g, 'A') is True

def test_is_cycle_dft():
    """Perform if graph has a cycle with breadth first traversal."""
    from graph import Graph
    from graph2 import is_cycle_bfs
    assert is_cycle_bfs(g, 'A') is True

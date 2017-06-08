"""Module for testing graph2.py."""
import pytest
from graph import Graph


g = Graph()

g.add_edge('c', 'f')
g.add_edge('c', 'g')

g.add_edge('e', 'j')
g.add_edge('e', 'k')

g.add_edge('d', 'h')
g.add_edge('d', 'i')

g.add_edge('b', 'e')
g.add_edge('b', 'd')

g.add_edge('a', 'c')
g.add_edge('a', 'b')


def test_depth_first_traversal():
    """."""
    from graph2 import depth_first_traversal
    assert g.depth_first_traversal() is ['A','B','D','H','I','E','J','K','C','F','G']


def test_breadth_first_traversal():
    """."""
    from graph2 import breadth_first_traversal
    assert g.breadth_first_traversal() is ['A','B','C','D','E','F','G','H','I','J','K']

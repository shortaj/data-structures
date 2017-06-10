"""Module for testing graph.py."""

from graph import Graph
import pytest

g = Graph()

g.add_edge('A', 'B')
g.add_edge('A', 'C')

# g.add_edge('B', 'D')
# g.add_edge('B', 'E')

# g.add_edge('C', 'F')
# g.add_edge('C', 'G')

# g.add_edge('D', 'H')
# g.add_edge('D', 'I')

# g.add_edge('E', 'J')
# g.add_edge('E', 'K')


def test_Graph_nodes():
    """Test self.nodes() returns a list."""
    assert isinstance(g.nodes(), list) is True


def test_Graph_edges():
    """Test edges return edgelist."""
    assert g.edges() == [('A', 'B'), ('A', 'C')]


def test_add_node0():
    """Test add a node to Graph() if node not in dictionary."""
    g.add_node('a')
    assert 'a' in g.nodes()
    assert len(g.nodes()) == 4


def test_add_node1():
    """Test not add a node to Graph() if node already in dictionary."""
    g.add_node('a')
    assert len(g.nodes()) == 4


def test_add_edge0():
    """Test add v1-v2 edge to Graph() if not already exist."""
    g.add_edge('B', 'D')
    # assert g.edges() == [('A', 'B'), ('A', 'C'), ('B', 'D')]
    assert ('B', 'D') in g.edges()


def test_add_edge1():
    """Test not add v1-v2 edge to Graph() if already exist."""
    g.add_edge('A', 'B')
    # assert g.edges() == [('A', 'B'), ('A', 'C'), ('B', 'D')]
    assert len(g.edges()) == 3


def test_del_node0():
    """Test error message if node not in dictionary."""
    with pytest.raises(KeyError):
        g.del_node('b')


def test_del_node1():
    """Test delete a node if node in dictionary."""
    g.del_node('a')
    # assert g.nodes() == ['A', 'B', 'C', 'D']
    assert len(g.nodes()) == 4


def test_del_edge0():
    """Test error message if nodes not exist."""
    with pytest.raises(ValueError):
        g.del_edge('z', 'D')


def test_del_edge1():
    """Test error message if edge not exist."""
    with pytest.raises(ValueError):
        g.del_edge('A', 'y')


def test_del_edge2():
    """Test egdg is deleted from Graph() if edge exists."""
    g.del_edge('B', 'D')
    assert g.edges() == [('A', 'B'), ('A', 'C')]


def test_has_node():
    """True if graph contains node.data."""
    assert g.has_node('A') is True


def test_neighbors0():
    """Test error message if nodes not exist."""
    with pytest.raises(KeyError):
        g.neighbors('z')


def test_neighbors1():
    """Test list of all nodes containing val by edges."""
    assert g.neighbors('A') == ['B', 'C']


def test_adjacent():
    """True if an edge connects val1 and val2."""
    assert g.adjacent('A', 'B') is True

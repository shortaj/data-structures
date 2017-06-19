"""Module for testing graph.py."""

from graph import Graph
import pytest

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


def test_Graph_nodes_instance():
    """Test self.nodes() returns a list."""
    assert isinstance(g.nodes(), list) is True


def test_Graph_edges_num_edges():
    """Test edges return edgelist length."""
    assert len(g.edges()) == 10


def test_Graph_edges_verify():
    """Test edges verify edges."""
    assert ('A', 'B') in g.edges()
    assert ('E', 'J') in g.edges()
    assert ('C', 'G') in g.edges()


def test_add_node_not_exist():
    """Test add a node to Graph() if node not in dictionary."""
    g.add_node('a')
    assert 'a' in g.nodes()
    assert len(g.nodes()) == 12


def test_add_node_exist():
    """Test not add a node to Graph() if node already in dictionary."""
    g.add_node('a')
    assert len(g.nodes()) == 12


def test_add_edge_not_exist():
    """Test add v1-v2 edge to Graph() if not already exist."""
    g.add_edge('G', 'a')
    assert ('G', 'a') in g.edges()
    assert len(g.edges()) == 11


def test_add_edge_exist():
    """Test not add v1-v2 edge to Graph() if already exist."""
    g.add_edge('A', 'B')
    assert len(g.edges()) == 11


def test_del_node_err():
    """Test error message if node not in dictionary."""
    with pytest.raises(KeyError):
        g.del_node('b')


def test_del_edge_not_exist_node():
    """Test error message if node not exist."""
    with pytest.raises(ValueError):
        g.del_edge('z', 'D')


def test_del_edge_not_exist_edge():
    """Test error message if edge not exist."""
    with pytest.raises(ValueError):
        g.del_edge('A', 'a')


def test_del_edge_exist():
    """Test egde is deleted from Graph() if edge exists."""
    g.del_edge('G', 'a')
    assert len(g.edges()) == 10
    assert ('G', 'a') not in g.edges()


def test_del_node_exist():
    """Test delete a node if node in dictionary."""
    g.del_node('a')
    assert len(g.nodes()) == 11


def test_has_node_exist():
    """True if graph contains node.data."""
    assert g.has_node('A') is True


def test_has_node_not_exist():
    """True if graph contains node.data."""
    assert g.has_node('z') is False


def test_neighbors_err():
    """Test error message if nodes not exist."""
    with pytest.raises(KeyError):
        g.neighbors('z')


def test_neighbors_list():
    """Test list of all nodes containing val by edges."""
    assert g.neighbors('A') == ['B', 'C']
    assert g.neighbors('B') == ['D', 'E']
    assert g.neighbors('G') == []


def test_adjacent():
    """True if an edge connects val1 and val2."""
    assert g.adjacent('C', 'F') is True
    assert g.adjacent('D', 'I') is True

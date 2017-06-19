"""Module for testing weighted_graph.py."""

from weighted_graph import WeightedGraph
import pytest

g = WeightedGraph()

g.add_edge('A', 'B', 10)
g.add_edge('A', 'C', 20)

g.add_edge('B', 'D', 15)
g.add_edge('C', 'D', 30)

g.add_edge('B', 'E', 50)
g.add_edge('D', 'E', 30)

g.add_edge('E', 'F', 5)
g.add_edge('F', 'G', 2)


def test_WeightedGraph_nodes_instance():
    """Test self.nodes() returns a list."""
    assert isinstance(g.nodes(), list) is True


def test_WeightedGraph_nodes_tabulate():
    """Return list of nodes."""
    assert sorted(g.nodes()) == ['A', 'B', 'C', 'D', 'E', 'F', 'G']


def test_WeightedGraph_edges_num_edges():
    """Test edges return edgelist length."""
    assert len(g.edges()) == 8


def test_WeightedGraph_edges_verify():
    """Test edges verify edges."""
    assert ('A', 'B') in g.edges()
    assert ('A', 'C') in g.edges()
    assert ('B', 'D') in g.edges()
    assert ('C', 'D') in g.edges()
    assert ('B', 'E') in g.edges()
    assert ('D', 'E') in g.edges()
    assert ('E', 'F') in g.edges()
    assert ('F', 'G') in g.edges()


def test_add_node_not_exist():
    """Test add a node to Graph() if node not in dictionary."""
    g.add_node('a')
    assert 'a' in g.nodes()
    assert len(g.nodes()) == 8


def test_add_node_exist():
    """Test not add a node to Graph() if node already in dictionary."""
    g.add_node('a')
    assert len(g.nodes()) == 8


def test_add_edge_not_exist():
    """Test add v1-v2 edge to WeightedGraph() if not already exist."""
    g.add_edge('G', 'a')
    assert ('G', 'a') in g.edges()
    assert len(g.edges()) == 9


def test_add_edge_exist():
    """Test not add v1-v2 edge to Graph() if already exist."""
    g.add_edge('A', 'B')
    assert len(g.edges()) == 9


def test_del_node_err():
    """Test error message if node not in dictionary."""
    with pytest.raises(ValueError):
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
    assert len(g.edges()) == 8
    assert ('G', 'a') not in g.edges()


def test_del_node_exist():
    """Test delete a node if node in dictionary."""
    g.del_node('a')
    assert len(g.nodes()) == 7


def test_has_node_exist():
    """True if graph contains node.data."""
    assert g.has_node('A') is True


def test_has_node_not_exist():
    """True if graph contains node.data."""
    assert g.has_node('z') is False


def test_neighbors_err():
    """Test error message if nodes not exist."""
    with pytest.raises(ValueError):
        g.neighbors('z')


def test_neighbors_list():
    """Test list of all nodes containing val by edges."""
    assert g.neighbors('A') == {'B': 10, 'C': 20}
    assert g.neighbors('B') == {'D': 15, 'E': 50}
    assert g.neighbors('G') == {}


def test_adjacent_val1_not_connects_val2():
    """True if an edge connects val1 and val2."""
    assert g.adjacent('C', 'F') is False


def test_adjacent_val1_connects_val2():
    """True if an edge connects val1 and val2."""
    assert g.adjacent('A', 'B') is True

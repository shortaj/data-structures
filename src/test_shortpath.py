"""Module for testing shortpath.py."""
import pytest
from shortpath import Graphplus
from time import time

g = Graphplus()
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'C', 5)
g.add_edge('B', 'D', 10)
g.add_edge('C', 'E', 3)
g.add_edge('E', 'D', 4)
g.add_edge('D', 'F', 11)

gg = Graphplus()
gg.add_edge('s', 'u', 10)
gg.add_edge('s', 'x', 5)
gg.add_edge('u', 'v', 1)
gg.add_edge('u', 'x', 2)
gg.add_edge('v', 'y', 4)
gg.add_edge('x', 'u', 3)
gg.add_edge('x', 'v', 9)
gg.add_edge('x', 'y', 2)
gg.add_edge('y', 's', 7)
gg.add_edge('y', 'v', 6)


def test_dijkstrategy():
    """Perform dijkstra on single source path."""
    from shortpath import dijkstrategy
    assert dijkstrategy(g, 'A', 'F') == (['A', 'C', 'E', 'D', 'F'], 20)


def test_dijkstrategy():
    """Perform dijkstra on single source path with cycle."""
    from shortpath import dijkstrategy
    assert dijkstrategy(gg, 's', 'v') == (['s', 'x', 'u', 'v'], 9)


def test_time_funk():
    """Time Dijkstra performance."""
    from shortpath import time_funk
    from shortpath import dijkstrategy
    print('Dijkstra', time_funk(g, dijkstrategy, 'A', 'F'))
    assert 0 == 0

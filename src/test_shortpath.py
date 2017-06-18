"""Module for testing shortpath.py."""
import pytest
from shortpath import Graphplus
from time import time

gd1 = Graphplus()
gd1.add_edge('A', 'B', 4)
gd1.add_edge('A', 'C', 2)
gd1.add_edge('B', 'C', 5)
gd1.add_edge('B', 'D', 10)
gd1.add_edge('C', 'E', 3)
gd1.add_edge('E', 'D', 4)
gd1.add_edge('D', 'F', 11)

gd2 = Graphplus()
gd2.add_edge('s', 'u', 10)
gd2.add_edge('s', 'x', 5)
gd2.add_edge('u', 'v', 1)
gd2.add_edge('u', 'x', 2)
gd2.add_edge('v', 'y', 4)
gd2.add_edge('x', 'u', 3)
gd2.add_edge('x', 'v', 9)
gd2.add_edge('x', 'y', 2)
gd2.add_edge('y', 's', 7)
gd2.add_edge('y', 'v', 6)

gb1 = Graphplus()
gb1.add_edge('A', 'B', -1)
gb1.add_edge('A', 'C', 4)
gb1.add_edge('B', 'C', 3)
gb1.add_edge('B', 'D', 2)
gb1.add_edge('B', 'E', 2)
gb1.add_edge('D', 'B', 1)
gb1.add_edge('D', 'C', 5)
gb1.add_edge('E', 'D', -3)

gb2 = Graphplus()
gb2.add_edge('A', 'B', 5)
gb2.add_edge('A', 'C', 4)
gb2.add_edge('C', 'B', -6)
gb2.add_edge('B', 'D', 3)
gb2.add_edge('D', 'C', 2)


def test_dijkstrategy_nocycle():
    """Perform Dijkstra algorithm on single source path."""
    from shortpath import dijkstrategy
    assert dijkstrategy(gd1, 'A', 'F') == (['A', 'C', 'E', 'D', 'F'], 20)


def test_dijkstrategy_cycle():
    """Perform Dijkstra algorithm on single source path with cycle."""
    from shortpath import dijkstrategy
    assert dijkstrategy(gd2, 's', 'v') == (['s', 'x', 'u', 'v'], 9)


def test_time_funk():
    """Time Dijkstra algorithm performance."""
    from shortpath import time_funk
    from shortpath import dijkstrategy
    print('Dijkstra', time_funk(gd1, dijkstrategy, 'A', 'F'))
    assert 0 == 0


def test_bellford_negative_edge():
    """Perform Bellman-Ford algorithm on single source path."""
    from shortpath import bellford
    assert bellford(gb1, 'A', 'C') == (['A', 'B', 'C'], 2)


def test_bellford_negative_cycle():
    """Perform Bellman-Ford algorithm on negative cycle."""
    from shortpath import bellford
    from shortpath import MyException
    with pytest.raises(MyException):
        bellford(gb2, 'A', 'B')

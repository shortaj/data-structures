"""Docstring for Dijkstra and Bellman-Ford algorithms."""
from collections import deque
from time import time


class MyException(Exception):
    """Bellman-Ford negative cycle exception."""
    pass


class Graphplus(object):
    """Docstring for python graph with weights."""

    def __init__(self, graph={}):
        """Initialize graph node."""
        graph = {}
        self._graph = graph
        self.wt = {}

    def nodes(self):
        """Return a list of all nodes."""
        return list(self._graph.keys())

    def edges(self):
        """Return a list of all edges."""
        edgelist = []
        for node in self._graph:
            for neighbor in self._graph[node]:
                if (node, neighbor) not in self._graph:
                    edgelist.append((node, neighbor, self._graph[node][neighbor]))
        return edgelist

    def add_node(self, val):
        """Add a node to graph."""
        # if val not in self._gdict:
        #     self._gdict[val] = []
        self._graph.setdefault(val, {})

    def add_edge(self, val1, val2, weight):
        """Add an edge from val1 to val2

        Inserts val1, val2 into edgelist if they don't
        already exist.
        """
        if val1 not in self._graph:
            self.add_node(val1)
        if val2 not in self._graph:
            self.add_node(val2)
        if val2 in self._graph[val1]:
            # self._graph[val1].remove()
            return
        self._graph[val1][val2] = self.wt[(val1, val2)] = weight

    def neighbors(self, val):
        """Return the list of all nodes"""
        return list(self._graph[val].keys())


def dijkstrategy(gy, start_val, end_val):
    """Dijkstra algorithm."""
    visited, path = {start_val: 0}, {}
    nodes = set(gy.nodes())
    while nodes:
        begin_node = None
        for node in nodes:
            if node in visited:
                if begin_node is None:
                    begin_node = node
                elif visited[node] < visited[begin_node]:
                    begin_node = node
        if begin_node is None: break
        nodes.remove(begin_node)
        current_weight = visited[begin_node]
        for edge in gy.neighbors(begin_node):
            weight = current_weight + gy.wt[(begin_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = begin_node
    Path = deque()
    _end = path[end_val]
    while _end != start_val:
        Path.appendleft(_end)
        _end = path[_end]
    Path.appendleft(start_val)
    Path.append(end_val)
    return list(Path), visited[end_val]


def time_funk(g, funk, start_val, end_val):
    """Time function performance."""
    t0 = time()
    funk(g, start_val, end_val)
    t1 = time()
    return 'search time ' + str(round(t1 - t0, 5)) + " sec."


def bellford(gy, start_val, end_val):
    """Bellman-Ford algorithm."""
    visited, path = {}, {}
    nodes = gy.nodes()
    for i in nodes:
        visited[i] = float('Inf')
        path[i] = None
    visited[start_val] = 0
    for i in range(len(nodes) - 1):
        for u in nodes:
            for v in gy.neighbors(u):
                if visited[v] > visited[u] + gy.wt[(u, v)]:
                    visited[v] = visited[u] + gy.wt[(u, v)]
                    path[v] = u
    for u in nodes:
        for v in gy.neighbors(u):
            if visited[v] > visited[u] + gy.wt[(u, v)]:
                raise MyException("Graph contains negative cycles, no cheapest path.")
    Path = deque()
    _end = path[end_val]
    while _end != start_val:
        Path.appendleft(_end)
        _end = path[_end]
    Path.appendleft(start_val)
    Path.append(end_val)
    return list(Path), visited[end_val]

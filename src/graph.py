"""Module for graph with single direction.

graph = {

     "a"    :["c", "b"],
     "b"    :["a", "c"],
     "c"    :["a", "b", "d", "e"],
     "d"    :["c", "e"],
     "e"    :["d", "c"],
     "f"    :[],
     "g"    :[]

}

edge = [
        ('a', 'c'), ('a', 'b'),('b', 'a'),
        ('b', 'c'), ('c', 'a'), ('c', 'b'),
        ('c', 'd'), ('c', 'e'), ('e', 'c'),
        ('e', 'd'), ('d', 'e'), ('d', 'c')
]

"""


class Graph(object):
    """Docstring for python graph."""

    def __init__(self, graph={}):
        """Initialize graph node."""
        self._graph = graph

    def nodes(self):
        """Return a list of all nodes."""
        return list(self._graph.keys())

    def edges(self):
        """Return a list of all edges."""
        edgelist = []
        for node in self._graph:
            for neighbor in self._graph[node]:
                if (node, neighbor) not in self._graph:
                    edgelist.append((node, neighbor))
        return edgelist

    def add_node(self, val):
        """Add a node to graph."""
        # if val not in self._graph:
        #     self._graph[val] = []
        self._graph.setdefault(val, [])

    def add_edge(self, val1, val2):
        """Add an edge from val1 to val2

        Inserts val1, val2 into edgelist if they don't
        already exist."""
        if val1 not in self._graph:
            self.add_node(val1)
        if val2 not in self._graph:
            self.add_node(val2)
        if val2 in self._graph[val1]:
                self._graph[val1].remove(val2)
        self._graph[val1].append(val2)

    def del_node(self, val):
        """Delete a node to graph."""
        if not self.has_node(val):
            raise KeyError('Key doesn not exist.')
        self._graph.pop(val, None)
        for key in self._graph:
            if val in self._graph[key]:
                self._graph[key].remove[val]

    def del_edge(self, val1, val2):
        """Delete an edge to graph."""
        if not val1 in self._graph or not val2 in self._graph:
            raise ValueError('graph does not have one of the nodes.')
        if not val2 in self._graph[val1]:
            raise ValueError('graph does not have edge.')
        self._graph[val1].remove[val2]

    def has_node(self, val):
        """True if graph contains node.data."""
        return val in self._graph

    def neighbors(self, val):
        """Return the list of all nodes

        connected to the node containing 'val' by edges."""
        if not self.has_node(val):
            raise KeyError('Key doesn not exist.')
        return self._graph[val]

    def adjacent(self, val1, val2):
        """True if an edge connects val1 and val2."""
        return val2 in self._graph[val1]

    def alone_node(self):
        """Return a list of all not connected nodes."""
        alone = []
        for node in self._graph:
            if not self._graph[node]:
                alone.append(node)
        return alone

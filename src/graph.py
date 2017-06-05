"""Module for python graph.

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

    def __init__(self, gdict={}):
        """Initialize graph node."""
        self._gdict = gdict

    def nodes(self):
        """Return a list of all nodes."""
        return list(self._gdict.keys())

    def edges(self):
        """Return a list of all edges."""
        edgelist = []
        for node in self._gdict:
            for neighbor in self._gdict[node]:
                if (node, neighbor) not in self._gdict:
                    edgelist.append((node, neighbor))
        return edgelist

    def add_node(self, val):
        """Add a node to graph."""
        if val not in self._gdict:
            self._gdict[val] = []

    def add_edge(self, val1, val2):
        """Add a new edge to graph."""
        if val1 in self._gdict:
            self._gdict[val1].append(val2)
        else:
            self._gdict[val2].append(val1)

    def del_node(self, val):
        """Delete a node to graph."""
        if not self.has_node(val):
            raise KeyError('Key doesn not exist.')
        self._gdict.pop(val, 0)

    def del_edge(self, val1, val2):
        """Delete an edge to graph."""
        self._gdict[val1].remove[val2]
        self._gdict[val2].remove[val1]

    def has_node(self, val):
        """True if graph contains node.data."""
        return val in self._gdict

    def neighbors(self, val):
        """Return the list of all nodes \
        connected to the node containing ‘val’ by edges."""
        if not self.has_node(val):
            raise KeyError('Key doesn not exist.')
        return self._gdict[val]

    def adjacent(self, val1, val2):
        """True if an edge connects val1 and val2."""
        edge = self.edges()
        return True if (val1, val2) in edge else False

    def alone_node(self):
        """Return a list of all not connected nodes."""
        alone = []
        for node in self._gdict:
            if not self._gdict[node]:
                alone.append(node)
        return alone

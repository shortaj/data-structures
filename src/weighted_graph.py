
class WeightedGraph(object):
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
        if val not in self._graph:
            self.setdefault(val, {})

    def add_edge(self, val1, val2, weight=0):
        """Add an edge from val1 to val2

        Inserts val1, val2 into edgelist if they don't
        already exist.
        """
        self.add_node(val1)
        self.add_node(val2)
        if val2 not in self[val1]:
            self[val1][val2] = weight

    def del_node(self, val):
        """Delete a node to graph."""
        try:
            del self._graph[val]
            for key in self._graph:
                if val in self._graph[key]:
                    del self._graph[key][val]
        except KeyError:
            raise ValueError('Graph does not have value: ' + val)

    def del_edge(self, val1, val2):
        """Delete an edge to graph."""
        try:
            del self._graph[val1][val2]
        except KeyError:
            raise ValueError('Edge does not exist.')

    def has_node(self, val):
        """True if graph contains node.data."""
        return val in self._graph


    def neighbors(self, val):
        """Return the list of all nodes

        connected to the node containing 'val' by edges.
        """
        if val in self._graph:
            return self._graph[val]
        raise ValueError('Graph does not have value: ' + val)

    def adjacent(self, val1, val2):
        """True if an edge connects val1 and val2."""
        if val1 not in self._graph:
            raise ValueError('Graph does not have value: ' + val1)
        if val2 not in self._graph:
            raise ValueError('Graph does not have value: ' + val2)
        if val2 in self._graph[val1]:
            return True
        return False

"""."""


class Node(object):
    """Docstring for Node."""

    def __init__(self, data=None, next_node=None):
        """Initializer for the class instance."""
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    """Docstring for LinkedList."""

    def __init__(self, head=None):
        """Initializer for the class instance."""
        self.head = head
        self._length = 0
        if type(some_iterable) in [list,tuple, str]:
            for item in some_iterable:
                self._length += 1
                self.push(item)
        elif type(some_iterable) is not None:
            raise TypeError('Requires an iterable value.')


    def push(self, data):
        """Will insert the value ‘data’ at the head of the list."""
        if not val:
            raise ValueError('You must provide a not-null value.')
        new_node = Node(data, self.head)
        self.head = new_node
        self._length += 1

    def size(self):
        """Will return the length of the list."""
        return self._length


    def pop(self):
        """Will pop the first value off the head of the list and return it.
            Raises an exception with an appropriate message if there are no
            values to return.
        """
        if not self.head:
            raise IndexError('Cannot pop from an empty list.')
        popped = self.head
        self.head = self.head.next_node
        self._length -= 1
        return popped.data


    def search(self, node):
        """Will return the node containing ‘val’ in the list, if present,
            else None."""


    def remove(self, node):
        """ Will remove the given node from the list, wherever it might be
            (node must be an item in the list). If the node is not in the list,
             it should raise an exception with an appropriate message."""


    def display(self, ):
        """Will return a unicode string representing the list as if it were
            a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”."""


        def len(self, ):
            """Return the size of the list."""


        def print(self, ):
            """Return what the display() method returns."""

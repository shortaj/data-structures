"""The queue data structure."""


class Node(object):
    """Docstring for Node."""

    def __init__(self, data=None, previous_node=None, next_node=None):
        """Initializer for the class instance."""
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node


class Que(object):
    """Docstring for Que."""

    def __init__(self, data=None):
        """Initialize class instance."""
        self.head = None
        self.tail = None
        self._length = 0

        if type(data) in [list, tuple, str]:
            for item in data:
                self.enqueue(item)

        elif data is not None:
            raise TypeError('Requires an iterable value.')

    def enqueue(self, val):
        """Insert the value 'val' at the tail of the list."""
        if not val:
            raise ValueError('You must provide a not-null value.')
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        elif self._length >= 1:
            new_node = Node(val)
            last_tail = self.tail
            self.tail = new_node
            last_tail.previous_node = self.tail
            self.tail.next_node = last_tail
        self._length += 1
        return self

    def size(self):
        """Will return the length of the list."""
        return self._length

    def peek(self):
        """Return data of the head of the queue."""
        if not self.head:
            return None
        return self.head.data

    def dequeue(self):
        """Remove the head value and return, raise exception."""
        if not self.head:
            raise IndexError('Cannot dequeue from an empty list.')
        shifted = self.head
        shifted.previous_node is None
        self.head = self.head.previous_node
        self.head.next_node = None
        self._length -= 1
        return shifted.data

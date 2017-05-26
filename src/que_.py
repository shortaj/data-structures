# -*- coding: utf-8 -*-
"""."""


class Node(object):
    """Docstring for Node."""

    def __init__(self, data=None, previous_node=None, next_node=None):
        """Initializer for the class instance."""
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node


class Que(object):
    """Docstring for DoublyLink."""

    def __init__(self, data=None):
        """Initialize class instance."""
        self.head = None
        self.tail = None
        self._length = 0

        if type(data) in [list, tuple, str]:
            for item in data:
                self._length += 1
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
        elif self._length > 1:
            new_node = Node(val)
            current = self.head
            self.head = new_node
            self.head.next_node = current
            self.head.next_node.previous_node = self.head
        self._length += 1


    def size(self):
        """Will return the length of the list."""
        return self._length


    def dequeue(self):
        """Remove element at the head, raise exception."""
        if not self.tail:
            raise IndexError('Cannot shift from an empty list.')
        shifted = self.tail
        self.tail = self.tail.previous_node
        self.tail.next_node = None
        self._length -= 1
        return shifted.data





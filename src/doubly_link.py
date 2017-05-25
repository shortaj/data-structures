# -*- coding: utf-8 -*-
"""."""


class Node(object):
    """Docstring for Node."""

    def __init__(self, data=None, previous_node=None, next_node=None):
        """Initializer for the class instance."""
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node


class LinkedList(object):
    """Docstring for LinkedList."""

    def __init__(self, data=None):
        """Initializer for the class instance."""
        self.head = None
        self._length = 0
        self.nodelist = []
        if type(data) in [list, tuple, str]:
            for item in data:
                self._length += 1
                self.push(item)
                self.nodelist.append(item)
        elif data is not None:
            raise TypeError('Requires an iterable value.')


   def push(self, val):
        """Will insert the value 'val' at the head of the list."""
        if not val:
            raise ValueError('You must provide a not-null value.')
        new_node = Node(val, self.head)
        self.head.previous_node = new_node
        self.head = new_node
        self.nodelist.append(val)
        self._length += 1


    def size(self):
        """Will return the length of the list."""
        return self._length




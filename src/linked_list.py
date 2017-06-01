# -*- coding: utf-8 -*-
"""An example data structure of a linked list."""


class Node(object):
    """Docstring for Node."""

    def __init__(self, data=None, next_node=None):
        """Initializer for the class instance."""
        self.data = data
        self.next_node = next_node


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
        self.head = new_node
        self.nodelist.append(val)
        self._length += 1

    def size(self):
        """Will return the length of the list."""
        return self._length

    def pop(self):
        """Return the value of the head node after removing it."""
        if not self.head:
            raise IndexError('Cannot pop from an empty list.')
        popped = self.head
        self.head = self.head.next_node
        self._length -= 1
        self.nodelist.pop(popped.data)
        return popped.data

    def iterate_linked_list(self, node):
        """Allow for simple iterations over linked lists."""
        while node:
            yield node
            node = node.next_node

    def search(self, data):
        """Will return the node containing 'data' in the list, if present, else None."""
        current = self.head
        for node in self.iterate_linked_list(current):
            if node.data == data:
                return node
        return 'None'

    def remove(self, node):
        """Remove a specific node from the node list if it exists."""
        previous = None
        found = False
        current = self.head
        if current == node:
            self.head = current.next_node
            return
        while current is not None and found is False:
            if current == node and current.next_node is not None:
                previous.next_node = current.next_node
                current.next_node = None
                found = True
                break
            else:
                previous = current
                current = current.next_node
        if current is None:
            raise IndexError('Node not exist.')
        previous = self.head.next_node
        return self

    def display(self):
        """Return a tuple list of node data values."""
        return tuple(['({})'.format(item) for item in self.nodelist])

# -*- coding: utf-8 -*-

"""This module build linked list."""


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
        if type(data) in [list, tuple, str]:
            for item in data:
                self.push(item)
        elif data is not None:
            raise TypeError('Requires an iterable value.')

    def push(self, val):
        """Will insert the value 'val' at the head of the list."""
        if not val:
            raise ValueError('You must provide a not-null value.')
        new_node = Node(val, self.head)
        self.head = new_node
        self._length += 1

    def size(self):
        """Will return the length of the list."""
        return self._length

    def pop(self):
        """Pop head of list. Raises an exception if no value to return."""
        if not self.head:
            raise IndexError('Cannot pop from an empty list.')
        popped = self.head
        self.head = self.head.next_node
        self._length -= 1
        return popped.data

    def iterate_linked_list(self, node):
        """Allow for simple iterations over linked lists."""
        while node:
            yield node
            node = node.next_node

    def search(self, data):
        """Return node containing 'data' in the list, else None."""
        current = self.head
        for node in self.iterate_linked_list(current):
            if node.data == data:
                return node
        return 'None'

    def remove(self, node):
        """Remove node from list. Raise exception if node is not in the list."""
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

    def display(self):
        """
        Return a unicode string representing the list.

        As a Python tuple literal: “(12, ‘sam’, 37, ‘tango')”.
        """
        current = self.head
        print("( ")
        while current is not None:
            print(current.data) if hasattr(current, "data") else None
            print(current.next_node.data) if hasattr(current.next_node, "data") else None
            current = current.next_node
        print(")")

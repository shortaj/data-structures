# -*- coding: utf-8 -*-
"""."""


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
        """Will pop the first value off the head of the list and return it.
            Raises an exception with an appropriate message if there are no
            values to return.
        """
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
        """Will return the node containing 'data' in the list, if present,
            else None."""
        current = self.head
        for node in self.iterate_linked_list(current):
            if node.data == data:
                return node
        return 'None'


    def remove(self, node):
        """ Will remove the given node from the list, wherever it might be
            (node must be an item in the list). If the node is not in the list,
             it should raise an exception with an appropriate message."""
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
        """Will return a unicode string representing the list as if it were
            a Python tuple literal: “(12, ‘sam’, 37, ‘tango')”."""
        current = self.head
        print("( ")
        while current is not None:
            print(current.data) if hasattr(current, "data") else None
            print(current.next_node.data) if hasattr(current.next_node, "data") else None
            current = current.next_node
        print(")")

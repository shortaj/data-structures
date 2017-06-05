# -*- coding: utf-8 -*-
"""."""


class Node(object):
    """Docstring for Node."""

    def __init__(self, data=None, previous_node=None, next_node=None):
        """Initializer for the class instance."""
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node


class DoublyLink(object):
    """Docstring for DoublyLink."""

    def __init__(self, data=None):
        """Initialize class instance."""
        self.head = None
        self.tail = None
        self._length = 0

        if type(data) in [list, tuple, str]:
            for item in data:
                self._length += 1
                self.push(item)

        elif data is not None:
            raise TypeError('Requires an iterable value.')

    def push(self, val):
        """Insert the value 'val' at the head of the list."""
        if not val:
            raise ValueError('You must provide a not-null value.')
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        elif self._length >= 1:
            new_node = Node(val)
            current = self.head
            self.head = new_node
            self.head.next_node = current
            self.head.next_node.previous_node = self.head
        self._length += 1
        return self

    def size(self):
        """Will return the length of the list."""
        return self._length

    def append(self, val):
        """Append val at tail."""
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.next_node = new_node
        else:
            self.tail.next_node = new_node
            new_node.previous_node = self.tail
            self.tail = new_node
            self._length += 1
        return self

    def pop(self):
        """Pop head, raise exception."""
        if not self.head:
            raise IndexError('Cannot pop from an empty list.')
        popped = self.head
        if self._length < 2:
            return popped.data
        else:
            self.head = self.head.next_node
            self.head.previous_node = None
            self._length -= 1
        return popped.data

    def shift(self):
        """Remove last value and return, raise exception."""
        if not self.tail:
            raise IndexError('Cannot shift from an empty list.')
        shifted = self.tail
        self.tail = self.tail.previous_node
        self.tail.next_node = None
        self._length -= 1
        return shifted.data

    def iterate_linked_list(self, node):
        """Allow for simple iterations over linked lists."""
        while node:
            yield node
            node = node.next_node

    def search(self, data):
        """Return node containing 'data' in list if present, else None."""
        current = self.head
        for node in self.iterate_linked_list(current):
            if node.data == data:
                return node
        return None

    def remove(self, val):
        """Remove first instance, raise exception."""
        node = self.search(val)
        if node:
            if node.previous_node is None:
                self.pop()
            elif node.next_node is None:
                self.shift()
            else:
                self._length -= 1
                node.previous_node.next_node = node.next_node
                node.next_node.previous_node = node.previous_node
        return self

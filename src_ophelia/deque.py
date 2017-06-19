"""The Deque data structure."""


class Node(object):
    """Docstring for Node."""

    def __init__(self, data=None, previous_node=None, next_node=None):
        """Initializer for the class instance."""
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node


class Deque(object):
    """Docstring for Deque."""

    def __init__(self, data=None):
        """Initialize class instance."""
        self.head = None
        self.tail = None
        self._length = 0

        if type(data) in [list, tuple, str]:
            for item in data:
                self.append(item)

        elif data is not None:
            raise TypeError('Requires an iterable value.')

    def append(self, val):
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

    def appendleft(self, val):
        """Insert the value 'val' at the head of the list."""
        if not val:
            raise ValueError('You must provide a not-null value.')
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        elif self._length >= 1:
            new_node = Node(val)
            last_head = self.head
            self.head = new_node
            last_head.next_node = self.head
            self.head.previous_node = last_head
        self._length += 1
        return self

    def size(self):
        """Will return the length of the list."""
        return self._length

    def peekleft(self):
        """Return data of the tail of the queue."""
        if not self.head:
            return None
        return self.head.data

    def peek(self):
        """Return data of the tail of the queue."""
        if not self.tail:
            return None
        return self.tail.data

    def popleft(self):
        """Remove the head value and return, raise exception."""
        if not self.head:
            raise IndexError('Cannot pop from an empty list.')
        shifted = self.head
        if self._length < 2:
            self._length -= 1
            return shifted.data
        shifted.previous_node is None
        self.head = self.head.previous_node
        self.head.next_node = None
        self._length -= 1
        return shifted.data

    def pop(self):
        """Remove the tail value and return, raise exception."""
        if not self.head:
            raise IndexError('Cannot pop from an empty list.')
        shifted = self.tail
        if self._length < 2:
            self._length -= 1
            return shifted.data
        shifted.next_node is None
        self.tail = self.tail.next_node
        self.tail.previous_node = None
        self._length -= 1
        return shifted.data

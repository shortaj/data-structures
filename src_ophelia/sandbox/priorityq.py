"""Docstring for priority queue module."""


class Task(object):
    """Docstring for Task."""

    def __int__(self, data=None, next=None):
        """Initize Task."""
        # self.priority = data[0]
        # self.val = data[1]
        self.head = data
        self.next = None

    def display(self):
        """."""
        print((self.head))


class Priorityq(object):
    """Priority Queue data structure."""

    def __init__(self, data=None):
        """Initializer for the class instance."""
        self._length = 0
        self.priorityq = []
        if isinstance(data, tuple):
            for item in data:
                self.insert(data)
        elif data is not None:
            raise TypeError('Requires an iterable value.')

    def printlist(self):
        """."""
        return self.priorityq

    def pop(self):
        """Remove and return highest priority element from queue."""
        if not self.priorityq:
            raise IndexError('Cannot pop from an empty list.')
        # popped = [item for item in self.priorityq if item[0] == 0]
        # self.priorityq = [i for i in self.priorityq if i != popped]
        peekpop = min(self.priorityq, key=lambda k: k[0])
        popped = self.priorityq.pop(self.priorityq.index(peekpop))
        self._length -= 1
        return popped

    def insert(self, data):
        """Insert a new value in queue."""
        # new_task = Task(data)
        # self.head = new_task
        self.priorityq.append(data)
        self._length += 1

    def size(self):
        """Return the length of queue."""
        return self._length

    def peek(self):
        """Return highest priority element in queue without remove."""
        if not self.priorityq:
            raise IndexError('Cannot peek into an empty list.')
        return min(self.priorityq, key=lambda k: k[0])

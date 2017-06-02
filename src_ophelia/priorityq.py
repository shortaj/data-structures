"""Docstring for priority queue module."""


class Task(object):
    """Docstring for Task."""

    def __int__(self, priority, val):
        self.priority = priority
        self.val = val

    def __lt__(self, other):
        return (self.priority, self.val) < (other.priority, other.val) 

class Priorityq(object):
    """Priority Queue data structure."""

    def __init__(self, data=None):
        """Initializer for the class instance."""
        self._length = 0
        self.priorityq = []
        if type(data) is tuple:
            for item in data:
                self.push(item)

    def pop(self):
        """Remove and return highest priority element from queue."""
        if not self.priorityq:
            raise IndexError('Cannot pop from an empty list.')
        # popped = [item for item in self.priorityq if item[0] == 0]
        # self.priorityq = [i for i in self.priorityq if i != popped]
        popidx = [y[0] for y in self.priorityq].index(0)
        popped = self.priorityq.pop(popidx)
        self._length -= 1
        return popped

    def insert(self, val, priority=0):
        """Insert a new value in queue."""
        if not val:
            raise ValueError('You must provide a string value to insert.')
        new_task = Task(val, priority)
        self.priorityq.append(new_task)
        self._length += 1

    def size(self):
        """Return the length of queue."""
        return self._length

    def peek(self)
        """return highest priority element in queue without remove."""
        if not self.priorityq:
            raise IndexError('Cannot pop from an empty list.')
        popidx = [y[0] for y in self.priorityq].index(0)
        return self.priorityq[popidx]

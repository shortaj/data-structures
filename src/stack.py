from Linked_linst import LinkedList


class Stack(object):
    """This module implements stack."""
    def __init__(self, data):
        """Init stack instance."""
        self._new_LinkedList = LinkedList(data)

    def push(self, value):
        """Add a value to the stack."""
        return self._new_LinkList.push(val)


    def pop(self):
        """Remove a value from stack and return."""
        if self.size() < 1:
            raise IndexError('Cannot pop from an empty list.')
        return self._new_LinkList.pop()


    def size(self):
        """Length."""
        return self._new_LinkedList.size()
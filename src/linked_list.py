"""."""
a = LinkedLict([1, 2, 3])


class Node(object):
    """Docstring for Node."""

    def __init__(self, data=None, next_node=None):
        """Initializer for the class instance."""
        self.data = data
        self.next_node = next_node


    def get_data(self):
        return self.data


    def get_next(self):
        return self.next_node


    def set_next(self, new_next):
        try:
            self.next_node = new_next



class LinkedList(object):
    """Docstring for LinkedList."""

    def __init__(self, head=None):
        """Initializer for the class instance."""
        self.head = head

    def push(self, data):
        """Will insert the value ‘val’ at the head of the list."""
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        """Will return the length of the list."""
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count


    def push(self, val) = val:
        """Will insert the value ‘val’ at the head of the list."""


    def pop(self, ):
        """Will pop the first value off the head of the list and return it.
            Raises an exception with an appropriate message if there are no
            values to return."""


    def search(self, node):
        """Will return the node containing ‘val’ in the list, if present,
            else None."""


    def remove(self, node):
        """ Will remove the given node from the list, wherever it might be
            (node must be an item in the list). If the node is not in the list,
             it should raise an exception with an appropriate message."""


    def display(self, ):
        """Will return a unicode string representing the list as if it were
            a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”."""


        def len(self, ):
            """Return the size of the list."""


        def print(self, ):
            """Return what the display() method returns."""

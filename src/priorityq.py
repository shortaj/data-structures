"""."""


class Node(object):
    """docstring for Node."""

    def __init__(self, data=None, priority=None, parent=None, sibling=None, left_child=None, right_child=None):
        self.data = data
        self.priority = priority
        self.parent = parent
        self.sibling = sibling
        self.children = children


class PriotityQ(object):
    """Docstring for priorityq heap."""

    def __init__(self, data=None, priority=None):
        """Initializer for the class instance."""
        self.root = None
        self._length = 0
        if data and priority:
            for i, x in data, priority:
                self.push(i, x)

    def pop(self):
        """Remove top value in heap."""
        if self._length == 0:
            raise IndexError("empty list")
        min_value = self.heaplist[0]
        self.heaplist[0] = self.heaplist[-1]
        del self.heaplist[-1]
        self._length -= 1
        self.percolatdown()
        return min_value

    def push(self, val, priority=None):
        """Put a new value in heap."""
        new_node = Node(val, priority)
        if self._length is 0:
            self.root = new_node
        elif not self.root.left_child:
            self.root.left_child = new_node



        self._length += 1
        self.percolateup(self._length)

    def size(self):
        """Return the length of heap."""
        return self._length

    def percolateup(self, totem):
        """Move up length of heap."""
        while totem // 2 > 0:

            if self.heaplist[totem - 1] < self.heaplist[totem // 2 - 1]:
                temp = self.heaplist[totem // 2 - 1]
                self.heaplist[totem // 2 - 1] = self.heaplist[totem - 1]
                self.heaplist[totem - 1] = temp
            totem = totem // 2

    def percolatdown(self):
        """Move down length of heap."""
        idx = 0
        while idx <= self._length // 2 - 1:
            leftchildidx, rightchildidx = idx * 2 + 1, idx * 2 + 2
            minchildidx = leftchildidx if self.heaplist[rightchildidx] > self.heaplist[leftchildidx] else rightchildidx
            if self.heaplist[idx] > self.heaplist[minchildidx]:
                temp = self.heaplist[idx]
                self.heaplist[idx] = self.heaplist[minchildidx]
                self.heaplist[minchildidx] = temp
        idx += 1

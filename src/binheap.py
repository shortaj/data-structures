"""The binary data structure.

unit tests:
l1 = Binheap([6,7,12,10,15,17,5])
print(l1.heaplist) #[5, 7, 6, 10, 15, 17, 12]
l2 = Binheap([5, 9, 11, 14, 18, 19, 21, 33, 17, 27])
print(l2.heaplist) #[5, 9, 11, 14, 18, 19, 21, 33, 17, 27]
l2.push(7)
print(l2.heaplist) #[5, 7, 11, 14, 9, 19, 21, 33, 17, 27, 18]
l2.pop()
print(l2.heaplist)  #[9, 14, 11, 17, 18, 19, 21, 33, 27]

"""


class Binheap(object):
    """Docstring for binary heap."""

    def __init__(self, data=None):
        """Initializer for the class instance."""
        self._length = 0
        if type(data) in [list, tuple]:
            if str in data:
                return "Only iterable numbers puh-leeze."
            for i in data:
                self.push(i)

    def push(self, val):
        """Add a new value to the Binheap."""
        if val not in self:
            self._length += 1
            list.append(self, val)
            self.percolate_up(len(self) - 1)

    def pop(self):
        """Remove top value in heap."""
        if self._length == 0:
            raise IndexError("empty list")
        root = self[0]
        self[0], self[-1] = self[-1], root
        root = list.pop(self, -1)
        self._length -= 1
        self.percolate_down()
        return root

    def size(self):
        """Return the length of heap."""
        return self._length

    def percolate_up(self, i):
        """Move up the tree of the heap."""
        while True:
            if self[i] < self[(i - 1) // 2]:
                temp = self[i]
                self[i], self[(i - 1) // 2] = self[(i - 1) // 2], temp
            i = (i - 1) // 2
            if i < 1:
                break

    def percolate_down(self):
        """Move down the tree of the heap."""
        idx = 0
        while idx * 2 + 1 <= self._length - 1:
            leftchildidx, rightchildidx = idx * 2 + 1, idx * 2 + 2
            minchildidx = leftchildidx if self[rightchildidx] > self[leftchildidx] else rightchildidx
            if self[idx] > self[minchildidx]:
                temp = self[idx]
                self[idx] = self[minchildidx]
                self[minchildidx] = temp
        idx += 1

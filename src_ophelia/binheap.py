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

    def __init__(self, data):
        """Initializer for the class instance."""
        self._length = 0
        self.heaplist = []
        for i in data:
            self.push(i)

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

    def push(self, val):
        """Put a new value in heap."""
        self.heaplist.append(val)
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

"""Test for binheap."""
import pytest


@pytest.fixture
def import_binheap():
    from binheap import Binheap
    return Binheap()


def test_Binheap_empty(import_binheap):
    """."""
    test_Binheap = import_binheap
    assert test_Binheap.heaplist == []
    assert test_Binheap._length == 0


def test_Binheap_size():
    """."""
    from binheap import Binheap
    test_Binheap = Binheap([1, 2, 3])
    assert test_Binheap._length == 3
    assert test_Binheap.size() == 3

def test_Binheap_pop():
    """."""
    from binheap import Binheap
    test_Binheap = Binheap([1, 2, 3])
    assert test_Binheap.pop() == 1
    assert test_Binheap.size() == 2

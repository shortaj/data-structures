"""Module for testing deque.py."""
import pytest


@pytest.fixture
def new_empty_list(data=None):
    """Make empty list."""
    from deque import Deque
    return Deque(data)


def test_deque_0(new_empty_list):
    """When a new head is created, its head is none."""
    assert new_empty_list.head is None
    assert new_empty_list.size() == 0


def test_deque_1():
    """Module add to the right of deque, head left, tail right."""
    ll = new_empty_list('ab')
    assert ll.head.data == "a"
    assert ll.tail == "b"
    assert ll.head.previous_node is None
    assert ll.tail.next_node is None


def test_deque_2():
    """Module add to the right of deque, head left, tail right."""
    ll = new_empty_list('abcdefg')
    assert ll.head.data == "a"
    assert ll.tail == "g"


def test_deque_append_right():
    """Module append val to the end of deque."""
    ll = new_empty_list('abcdefg')
    ll.append("h")
    assert ll.tail.data is "h"
    assert ll.tail.next_node.data == "g"


def test_deque_appendleft():
    """Module append val to the front of deque."""
    ll = new_empty_list('abcdefg')
    ll.appendleft("h")
    assert ll.head.data is "h"
    assert ll.head.previous_node.data == "a"


def test_deque_pop():
    """Module removes val from the end of deque."""
    ll = new_empty_list("abcdefg")
    ll.pop() is "g"
    assert ll.tail.data is "f"


def test_deque_popleft():
    """Module removes val from the front of deque."""
    ll = new_empty_list("abcdefg")
    assert ll.pop() == "g"
    assert ll.tail.data is "f"


def test_deque_pop_notexist():
    """Module raise exception when deque is empty."""
    ll = new_empty_list()
    with pytest.raises(IndexError):
        ll.pop()


def test_deque_popleft_notexist():
    """Module raise exception when deque is empty."""
    ll = new_empty_list()
    with pytest.raises(IndexError):
        ll.popleft()


def test_deque_peek():
    """Module returns a value that would have pop."""
    ll = new_empty_list("abcdefg")
    assert ll.peek() == "g"
    assert ll.tail.data == "g"


def test_deque_peekleft():
    """Module returns a value that would have popleft."""
    ll = new_empty_list("abcdefg")
    assert ll.peekleft() == "a"
    assert ll.head.data == "a"


def test_deque_size():
    """Module returns count of items in deque."""
    ll = new_empty_list("abcde")
    ll.size() == 5

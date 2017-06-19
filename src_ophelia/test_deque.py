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
    ll = new_empty_list('abcdefg')
    assert ll.head.data == "a"
    assert ll.tail.data == "g"
    assert ll.head.next_node is None
    assert ll.tail.previous_node is None


def test_deque_append():
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
    assert ll.pop() is "g"
    assert ll.tail.data is "f"


def test_deque_popleft():
    """Module removes val from the front of deque."""
    ll = new_empty_list("abcdefg")
    assert ll.popleft() == "a"
    assert ll.head.data is "b"


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


def test_deque_pop_one_node():
    """Module removes val from the end of deque of one node."""
    ll = new_empty_list("a")
    assert ll.pop() is "a"
    assert ll.size() == 0


def test_deque_popleft_one_node():
    """Module removes val from the front of deque of one node."""
    ll = new_empty_list("a")
    assert ll.popleft() == "a"
    assert ll.size() == 0


def test_deque_pop_two_node():
    """Module removes val from the end of deque of two node."""
    ll = new_empty_list("ab")
    assert ll.pop() is "b"
    assert ll.tail.data is "a"


def test_deque_popleft_two_node():
    """Module removes val from the front of deque of two node."""
    ll = new_empty_list("ab")
    assert ll.popleft() == "a"
    assert ll.head.data is "b"


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


def test_deque_data_notiterableErr():
    """Module raise exception deque datatype."""
    ll = new_empty_list()
    with pytest.raises(TypeError):
        ll = new_empty_list(1)


def test_deque_append_nullErr():
    """Module raise exception append null."""
    ll = new_empty_list()
    with pytest.raises(ValueError):
        ll.append("")


def test_deque_appendleft_nullErr():
    """Module raise exception append left null."""
    ll = new_empty_list()
    with pytest.raises(ValueError):
        ll.appendleft("")

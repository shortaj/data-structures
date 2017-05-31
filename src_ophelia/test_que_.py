# -*- coding: utf-8 -*-
"""Tests for que_.py."""

import pytest


LINKED_LIST_TABLE = [
    ([1, 2, 3], [1, 2, 3]),
    (["a", "b", "c"], ["a", "b", "c"])
]


@pytest.fixture
def new_empty_list():
    """Make empty list."""
    from que_ import Que
    return Que()


def test_que_0(new_empty_list):
    """When a new head is created, its head is none."""
    assert new_empty_list.head is None


def test_que_1(new_empty_list):
    """Module inserts a list."""
    from que_ import Que
    ll = Que("abc")
    assert ll.head.data == "a"
    assert ll.tail.data == "c"


# @pytest.mark.parametrize("arg, result", LINKED_LIST_TABLE)
# def test_node_data(arg, result):
#     """Test node class."""
#     from linked_list import Node
#     new_node = Node(arg)
#     assert new_node.data == result


def test_queue_enqueue_0(new_empty_list):
    """Module inserts ."""
    from que_ import Que
    ll = Que("abc")
    ll.enqueue(8)
    assert ll.tail.data is 8
    assert ll.head.data is "a"


def test_queue_enqueue_1(new_empty_list):
    """Module inserts the value 'val' at the head of the list."""
    from que_ import Que
    ll = Que("abc")
    ll.enqueue(1)
    ll.enqueue(2)
    ll.enqueue(3)
    assert ll.tail.data is 3


def test_dequeue_0():
    """Module dequeue."""
    from que_ import Que
    ll = Que([1, 2, 3])
    a = ll.dequeue()
    assert a is 1


def test_que_size(new_empty_list):
    """Module returns length of queue."""
    from que_ import Que
    ll = Que([1, 2, 3])
    assert ll.size() is 3


def test_peek_0():
    """Module peek."""
    from que_ import Que
    ll = Que()
    assert ll.peek() is None


def test_peek_1(new_empty_list):
    """Module peek."""
    from que_ import Que
    ll = Que([1, 2, 3])
    assert ll.peek() is 1

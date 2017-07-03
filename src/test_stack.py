# -*- coding: utf-8 -*-
"""Tests for stack.py."""
import pytest


def new_linked_list(data):
    """Make empty list."""
    from stack import Stack
    return Stack(data)


def test_stack_data():
    """Test stack class."""
    ll = new_linked_list([1, 2, 3])
    assert ll._new_LinkedList.head.data == 3
    assert ll._new_LinkedList.head.next_node.data == 2
    assert ll._new_LinkedList.head.next_node.next_node.data == 1


def test_stack_push():
    """Module inserts the value 'val' at the head of the stack."""
    ll = new_linked_list([1, 2, 3])
    ll._new_LinkedList.push(8)
    assert ll._new_LinkedList.head.data is 8
    assert ll.size() is 4


def test_stack_pop_0():
    """Module pops the first value off the head of the stack and return it.
    Raises an exception with an appropriate message if there are
    no values to return."""
    ll = new_linked_list([1, 2, 3])
    ll._new_LinkedList.pop()
    assert ll._new_LinkedList.head.data is 2
    assert ll.size() is 2


def test_stack_pop_1():
    """Module pops the first value off the head of the stack and return it.
    Raises an exception with an appropriate message if there are
    no values to return."""
    ll = new_linked_list([])
    with pytest.raises(IndexError):
        ll._new_LinkedList.pop()


def test_size():
    """Test if size is returning proper result."""
    ll = new_linked_list([1, 2, 3])
    assert ll.size() is 3

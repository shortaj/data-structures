# -*- coding: utf-8 -*-
"""Tests for linked_list.py."""


import pytest


LINKED_LIST_TABLE = [
    ([1, 2, 3], [1, 2, 3]),
    (["a", "b", "c"], ["a", "b", "c"])
]


@pytest.fixture
def new_empty_list():
    """Make empty list."""
    from linked_list import LinkedList
    return LinkedList()


def test_linked_list_0(new_empty_list):
    """When a new head is created, its head is none."""
    assert new_empty_list.head is None


def test_linked_list_remove_1():
    """Test the exception raise for remove."""
    from linked_list import LinkedList
    ll = LinkedList((1, 2, 3))
    with pytest.raises(IndexError):
        ll.remove(ll.search(8))


def test_linked_list_display():
    """Module return a unicode string representing the nodelist."""
    from linked_list import LinkedList
    ll = LinkedList((12, 'sam', 37, 'tango'))
    ll.display() is "('12', 'sam', '37', 'tango')"

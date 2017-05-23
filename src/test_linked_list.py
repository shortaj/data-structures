"""Tests for linked_list.py."""


import pytest


LINKED_LIST_TABLE = [
    ([1, 2, 3], [1, 2, 3]),
    (["a", "b", "c"], ["a", "b", "c"])
]


def test_linked_list_0():
    """When a new head is created, its head is none."""
    from linked_list import LinkedList
    ll = LinkedList()
    assert ll.head is None


def test_linked_list_1():
    """Module inserts a list."""
    from linked_list import LinkedList
    ll = LinkedList("abc")
    assert ll.head.data == "c"
    assert ll.head.next_node.data == "b"
    assert ll.head.next_node.next_node.data == "a"


@pytest.mark.parametrize("arg, result", LINKED_LIST_TABLE)
def test_node_data(arg, result):
    """Test node class."""
    from linked_list import Node
    new_node = Node(arg)
    assert new_node.data == result


def test_linked_list_push_0():
    """Module inserts the value 'val' at the head of the list."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push(8)
    assert ll.head.data is 8


def test_linked_list_push_1():
    """Module inserts the value 'val' at the head of the list."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push(1)
    ll.push("abc")
    ll.push(3)
    assert ll.head.data is 3


def test_linked_list_pop():
    """Module pops the first value off the head of the list and return it.
    Raises an exception with an appropriate message if there are
    no values to return."""
    from linked_list import LinkedList
    ll = LinkedList([1, 2, 3])
    ll.pop()
    assert ll.head.data is 2


def test_linked_list_size():
    """Module returns length of linked list."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    assert ll.size() is 3


# def test_linked_list_search_0(val):
#     """Module return the node not containing ‘val’ in the list."""
#     from linked_list import linked_list
#     ll = linked_list()
#     ll.push(8)
#     assert ll.search(3) is 'None'


# def test_linked_list_search_1(val):
#     """Module return the node containing ‘val’ in the list."""
#     from linked_list import linked_list
#     ll = linked_list()
#     ll.push(8)
#     ll.search(8)
#     assert ll.head.data is 8


# def test_linked_list_remove_0(node):
#     """Module remove the given node from the list.
#     If the node is not in the list, it should raise an exception
#     with an appropriate message."""
#     from linked_list import linked_list
#     ll = linked_list()
#     ll.push(1)
#     ll.push(2)
#     ll.push(3)
#     ll.remove(3)
#     assert ll.head.data is 2


# def test_linked_list_remove_1(node):
#     """Module remove the given node from the list.
#     If the node is not in the list, it should raise an exception
#     with an appropriate message."""
#     from linked_list import linked_list
#     ll = linked_list()
#     ll.push(8)
#     ll.remove(3)
#     raise Exception('No such node!')


# def test_linked_list_display():
#     """Module return a unicode string representing the list as if it were a
#     Python tuple literal: "(12, ‘sam’, 37, ‘tango’)"."""
#     from linked_list import linked_list
#     ll = linked_list()
#     ll.push(12)
#     ll.push('sam')
#     ll.push(37)
#     ll.push('tango')
#     ll.display() is "(12, ‘sam’, 37, ‘tango’)"

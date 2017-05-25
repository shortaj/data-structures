import pytest



@pytest.fixture
def new_empty_list(data=None):
    """Make empty list."""
    from doubly_link import DoublyLink
    return DoublyLink(data)


def test_linked_list_0(new_empty_list):
    """When a new head is created, its head is none."""
    # from linked_list import LinkedList
    # ll = LinkedList()
    assert new_empty_list.head is None


def test_linked_list_1():
    """Module inserts a list."""
    ll = new_empty_list('abc')
    assert ll.head.data == "c"
    assert ll.head.next_node.data == "b"
    assert ll.head.next_node.next_node.data == "a"
    assert ll.head.next_node.previous_node.data == "c"


# @pytest.mark.parametrize("arg, result", LINKED_LIST_TABLE)
# def test_node_data(arg, result):
#     """Test node class."""
#     from linked_list import Node
#     new_node = Node(arg)
#     assert new_node.data == result


# def test_linked_list_push_0():
#     """Module inserts the value 'val' at the head of the list."""
#     from linked_list import LinkedList
#     ll = LinkedList()
#     ll.push(8)
#     assert ll.head.data is 8


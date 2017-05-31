import pytest



@pytest.fixture
def new_empty_list(data=None):
    """Make empty list."""
    from doubly_link import DoublyLink
    return DoublyLink(data)


def test_doubly_link_0(new_empty_list):
    """When a new head is created, its head is none."""
    assert new_empty_list.head is None


def test_doubly_link_1():
    """Module inserts a list."""
    ll = new_empty_list('abc')
    assert ll.head.data == "c"
    assert ll.head.next_node.data == "b"
    assert ll.head.next_node.next_node.data == "a"
    assert ll.head.next_node.next_node.next_node is None


def test_doubly_link_append():
    """Module append val at end of list."""
    ll = new_empty_list('abc')
    ll.append(8)
    assert ll.tail.data is 8
    assert ll.tail.previous_node.data == 'a'


def test_doubly_link_push():
    """Module inserts val at the head of the list."""
    ll = new_empty_list('abc')
    ll.push(8)
    assert ll.head.data is 8
    assert ll.head.next_node.previous_node.data is 8


def test_doubly_link_pop_exist():
    """Module inserts val at the head of the list."""
    ll = new_empty_list('abc')
    assert ll.pop() == 'c'
    assert ll.head.data is 'b'
    assert ll.head.previous_node is None


def test_doubly_link_pop_notexist():
    """Module inserts val at the head of the list."""
    ll = new_empty_list()
    with pytest.raises(IndexError):
        ll.pop()


def test_doubly_link_shift_exist():
    """Module inserts val at the head of the list."""
    ll = new_empty_list('abc')
    assert ll.shift() == 'a'
    assert ll.tail.data == 'b'


def test_doubly_link_shift_notexist():
    """Module inserts val at the head of the list."""
    ll = new_empty_list()
    with pytest.raises(IndexError):
        ll.shift()


def test_doubly_link_remove_middle():
    """Test double link remove middle item."""
    ll = new_empty_list('abcde')
    ll.remove('d')
    assert ll.head.next_node.data == 'c'
    assert ll.head.next_node.previous_node.data == 'e'


def test_doubly_link_remove_head():
    """Test double link remove head."""
    ll = new_empty_list('abcde')
    ll.remove('e')
    assert ll.head.data == 'd'
    assert ll.head.previous_node is None

def test_doubly_link_remove_tail():
    """Test double link remove tail."""
    ll = new_empty_list('abcde')
    ll.remove('a')
    assert ll.tail.data == 'b'
    assert ll.tail.next_node is None

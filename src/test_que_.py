# -*- coding: utf-8 -*-
"""Tests for que_.py."""

import pytest


def test_empty_que():
    """When a new head is created, its head is none."""
    from que_ import Que
    new_que = Que()
    assert new_que.head is None


def test_new_que_multiple_nodes():
    """Module inserts a list."""
    from que_ import Que
    ll = Que('abc')
    assert ll.head.data == "a"
    assert ll.head.previous_node.data == "b"
    assert ll.head.previous_node.previous_node.data == "c"
    assert ll.head.next_node is None
    assert ll.tail.data == 'c'


def test_que_size():
    """Test that size gives accurate size."""
    from que_ import Que
    ll = Que('abcdef')
    assert ll.size() == 6


def test_que_peek():
    """Test that peek returns the head value."""
    from que_ import Que
    new_que = Que('abcdef')
    assert new_que.peek() == 'a'


def test_que_peek_empty():
    """Test that peeking into an empty list returns None."""
    from que_ import Que
    new_que = Que()
    assert new_que.peek() is None


def test_dequeue():
    """Test all aspects of dequeue."""
    from que_ import Que
    new_que = Que('abc')
    assert new_que.dequeue() == 'a'
    assert new_que.head.data == 'b'
    assert new_que.head.next_node is None
    assert new_que._length == 2


def test_dequeue_multiple():
    """Test multiple dequeues."""
    from que_ import Que
    new_que = Que('abcde')
    new_que.dequeue()
    new_que.dequeue()
    new_que.dequeue()
    new_que.dequeue()
    assert new_que.size() is 1

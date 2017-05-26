# -*- coding: utf-8 -*-
"""Tests for que_.py."""

import pytest


@pytest.fixture
def new_empty_list(data=None):
    """Make empty list."""
    from que_ import Que
    return Que(data)


def test_empty_que(new_empty_list):
    """When a new head is created, its head is none."""
    assert new_empty_list.head is None


def test_new_que_multiple_nodes():
    """Module inserts a list."""
    ll = new_empty_list('abc')
    assert ll.head.data == "a"
    assert ll.head.previous_node.data == "b"
    assert ll.head.previous_node.previous_node.data == "c"
    assert ll.head.next_node is None
    assert ll.tail.data == 'c'


def test_que_size():
    """."""
    new_que = new_empty_list('abcdef')
    assert new_que.size() == 6


def test_que_peek():
    """."""
    new_que = new_empty_list('abcdef')
    assert new_que.peek() == 'a'


def test_que_peek_empty():
    """."""
    new_que = new_empty_list()
    assert new_que.peek() is None


def test_dequeue():
    """."""
    new_que = new_empty_list('abc')
    assert new_que.dequeue() == 'a'
    assert new_que.head.data == 'b'
    assert new_que.head.next_node is None
    assert new_que._length == 2

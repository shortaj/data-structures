# -*- coding: utf-8 -*-
"""Tests for priorityq.py."""


import pytest


@pytest.fixture
def new_pq():
    """Make empty list."""
    from priorityq import Priorityq
    return Priorityq()


def test_priorityq_size(new_pq):
    """Initiat a new priority queue."""
    assert new_pq.size() == 0


def test_priorityq_insert(new_pq):
    """Module inserts values into a priority queue."""
    new_pq.insert(2, "red")
    new_pq.insert(3, "yellow")
    new_pq.insert(6, "black")
    new_pq.insert(2, "white")
    new_pq.insert(3, "purple")
    assert new_pq.size() == 5


def test_priorityq_peek():
    """Module assign value with default priority 0."""
    from priorityq import Priorityq
    pq = Priorityq((2, "red"), (3, "yellow"), (6, "black"), (2, "white"))
    pq.insert("purple")
    assert new_pq.peek() == 'purple'
    assert new_pq.size() == 5


def test_priorityq_pop(new_pq):
    """Module pop and return value with priority 0."""
    new_pq.insert(2, "red")
    new_pq.insert(3, "yellow")
    new_pq.insert(6, "black")
    new_pq.insert(2, "white")
    new_pq.insert("purple")
    assert new_pq.pop() == 'purple'
    assert new_pq.peek() == 'red'


def test_priorityq_raise_exception(new_pq):
    """Module pop from empty queue."""
    with pytest.raises(IndexError):
        new_pq.pop()

# -*- coding: utf-8 -*-
"""Tests for priorityq.py."""


import pytest


def test_priorityq_size():
    """Initiat a new priority queue."""
    from priorityq import Priorityq
    new_pq = Priorityq()
    assert new_pq.size() == 0


def test_priorityq_insert():
    """Module inserts values into a priority queue."""
    from priorityq import Priorityq
    pq = Priorityq()
    pq.insert((2, "red"))
    pq.insert((3, "yellow"))
    pq.insert((6, "black"))
    pq.insert((2, "white"))
    pq.insert((3, "purple"))
    assert pq.size() == 5


def test_priorityq_pop():
    """Module pop and return value with priority 0."""
    from priorityq import Priorityq
    pq = Priorityq()
    pq.insert((2, "red"))
    pq.insert((3, "yellow"))
    pq.insert((6, "black"))
    pq.insert((2, "white"))
    pq.insert((0, "purple"))
    assert pq.pop() == (0, 'purple')
    assert pq.peek() == (2, 'red')


def test_priorityq_raise_exception():
    """Module pop from empty queue."""
    from priorityq import Priorityq
    pq = Priorityq()
    with pytest.raises(IndexError):
        pq.pop()

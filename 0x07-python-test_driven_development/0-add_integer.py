#!/usr/bin/python3
"""Defines add_integer"""


def add_integer(a, b=98):
    """Computes the sum of two integers

    Args:
        a: integer to add to b
        b: integer to add to a
    Raises:
        TypeError: If a or b is not an integer or float.
    Returns:
        The sum of a and b
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b

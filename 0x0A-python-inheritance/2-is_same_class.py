#!/usr/bin/python3
"""Defines a is_same_class() function."""


def is_same_class(obj, a_class):
    """Checks of object is an exact instance of a class.

    Args:
        obj: Object to check.
        a_class: Class to check with.
    Returns:
        True if the object is an exact instance or False
    """
    return type(obj) == a_class

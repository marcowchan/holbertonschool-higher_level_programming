#!/usr/bin/python3
"""Defines a inherits_from() function."""


def inherits_from(obj, a_class):
    """Checks if an object inherits from a class.

    Args:
        obj: Object to check
        a_class: Class to check with

    Returns:
        True if the object inherits from the class or False
    """
    return isinstance(obj, a_class) and type(obj) != a_class

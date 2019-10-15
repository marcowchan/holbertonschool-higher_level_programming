#!/usr/bin/python3
"""Defines a lookup function."""


def lookup(obj):
    """Gets all attributes and methods of an object.

    Args:
        obj: Object to retrieve attributes and methods of.

    Returns:
        List of attributes and methods.
    """
    return dir(obj)

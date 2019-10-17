#!/usr/bin/python3
"""Defines a class_to_json function."""


def class_to_json(obj):
    """Gets the dictionary description of an object.

    Args:
        obj: Object to retrieve the dictionary from
    Returns:
        A dictionary description
    """
    return obj.__dict__

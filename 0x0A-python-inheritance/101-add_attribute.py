#!/usr/bin/python3
"""Defines a add_attribute() function."""


def add_attribute(obj, name, value):
    """Adds an attribute to an object.

    Args:
        obj: The object to add attributes to.
        name: The name of the attribute to add.
        value: The value of the attribute to add.

    Raises:
        TypeError: If the attribute could not be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)

#!/usr/bin/python3
"""Defines a to_json_string() function."""
import json


def to_json_string(my_obj):
    """Gets the JSON representation of an object.

    Args:
        my_obj: The object to serialize.
    Returns:
        The JSON string of the object.
    """
    return json.dumps(my_obj)

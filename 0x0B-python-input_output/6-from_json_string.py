#!/usr/bin/python3
"""Defines a from_json_string() function."""
import json


def from_json_string(my_str):
    """Deserializes a JSON string.

    Args:
        my_str: JSON string to Deserialize
    Returns:
        The deserialized object.
    """
    return json.loads(my_str)

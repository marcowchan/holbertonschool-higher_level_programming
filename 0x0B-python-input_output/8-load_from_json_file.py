#!/usr/bin/python3
"""Defines a load_from_json_file() function."""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename: The path and name of the file.
    Returns:
        The deserialized object.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())

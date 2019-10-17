#!/usr/bin/python3
"""Defines a save_to_json_file() function."""
import json


def save_to_json_file(my_obj, filename):
    """Saves an object to a file.

    Args:
        my_obj: The object to save.
        filename: The path and name of the save file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))

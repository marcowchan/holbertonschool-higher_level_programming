#!/usr/bin/python3
"""Defines an append_write() function."""


def append_write(filename="", text=""):
    """Appends a string to a file.

    Args:
        filename: The path and name of the file.
        text: The string to append.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
    return 0

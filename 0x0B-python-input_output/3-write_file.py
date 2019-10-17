#!/usr/bin/python3
"""Defines a write_file() function."""


def write_file(filename="", text=""):
    """Writes a string to a file.

    Args:
        filename: Path and name of the file.
        text: The string to write.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
    return 0

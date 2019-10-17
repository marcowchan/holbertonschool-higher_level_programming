#!/usr/bin/python3
"""Defines a read_file() function."""


def read_file(filename=""):
    """Prints the contents of a text file.

    Args:
        filename: The name and path of the file to print.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")

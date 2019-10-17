#!/usr/bin/python3
"""Defines a number_of_lines() function."""


def number_of_lines(filename=""):
    """Computes the number of lines in a file.

    Args:
        filename: The name and path of the file to print.
    Returns:
        The number of lines.
    """
    lines = 0
    with open(filename, "r", encoding="utf-8") as f:
        while f.readline() != "":
            lines += 1
    return lines

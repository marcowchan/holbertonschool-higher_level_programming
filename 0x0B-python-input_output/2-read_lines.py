#!/usr/bin/python3
"""Defines a read_lines() function."""


def read_lines(filename="", nb_lines=0):
    """Prints n number of lines of a file.

    Args:
        filename: Path and name of the file.
        nb_lines: Number of lines to print.
    """
    with open(filename, "r", encoding="utf-8") as f:
        if nb_lines <= 0:
            text = f.read()
            print(text, end="")
        for i in range(nb_lines):
            line = f.readline()
            if line == "":
                break
            print(line, end="")

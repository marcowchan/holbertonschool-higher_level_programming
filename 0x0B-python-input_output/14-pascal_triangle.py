#!/usr/bin/python3
"""Define a pascal_triangle() function."""


def pascal_triangle(n):
    """Returns a 2d list representing Pascal's triangle."""
    pascal = []
    prev = [1]
    if n > 0:
        pascal.append(prev)
        prev = prev.copy()
    for i in range(1, n):
        for j in range(len(prev[1:])):
            prev[j] += prev[1:][j]
        prev.insert(0, 1)
        pascal.append(prev)
        prev = prev.copy()
    return pascal

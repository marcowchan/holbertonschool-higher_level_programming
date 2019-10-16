#!/usr/bin/python3
"""Defines a MyInt class."""


class MyInt(int):
    """A class that inverts == and !=."""
    def __eq__(self, other):
        """Returns self != other."""
        return bool(self - other)

    def __ne__(self, other):
        """Returns self == other"""
        return not bool(self - other)

#!/usr/bin/python3
"""Defines a Base class."""


class Base:
    """A class with a counter attribute used to identify instances."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Sets the id of the instance.

        Args:
            id: The ID of the instance.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

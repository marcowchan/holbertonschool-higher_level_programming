#!/usr/bin/python3
"""Defines a Base class."""
import json


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

     @staticmethod
    def to_json_string(list_dictionaries):
        """Gets the json representation of a list of dictionaries."""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

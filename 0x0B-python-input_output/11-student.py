#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """A class with a first_name, last_name, and age attributes."""
    def __init__(self, first_name, last_name, age):
        """Initializes public attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets the dictionary representation of the instance."""
        return self.__dict__

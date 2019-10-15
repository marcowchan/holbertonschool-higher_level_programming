#!/usr/bin/python3
"""Defines a BaseGeometry class."""


class BaseGeometry:
    """A class with an integer_validation method."""
    def area(self):
        """Unimplemented area method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value.

        Args:
            name: A string name of the value.
            value: An integer value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is than or equal to 0.
        """
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

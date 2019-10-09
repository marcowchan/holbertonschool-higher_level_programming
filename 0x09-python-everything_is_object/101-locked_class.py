#!/usr/bin/python3
"""Defines a LockedClass class."""


class LockedClass:
    """A class with no attributes."""
    def __setattr__(self, name, value):
        """Only allows the dynamic creation of the 'first_name' attribute.

        Raises:
            AttributeError: If name is not 'first_name'.
        """
        if name == "first_name":
            object.__setattr__(self, 'first_name', value)
        else:
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name))

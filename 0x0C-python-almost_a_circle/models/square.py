#!/usr/bin/python3
"""Defines an Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that inherits from Rectangle with a size argument."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initalizes attributes."""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Returns the string representation of the Square instance."""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """Gets the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size attribute."""
        self.width = value
        self.height = value
        self.__size = value

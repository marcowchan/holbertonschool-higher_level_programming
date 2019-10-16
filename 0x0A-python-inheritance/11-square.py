#!/usr/bin/python3
"""Defines a Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that inherits from Rectangle."""
    def __init__(self, size):
        """Initalizes width and height to size."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Returns string representation of the Square."""
        return "[Square] {:d}/{:d}".format(self.__width, self.__height)

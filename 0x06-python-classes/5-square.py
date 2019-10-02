#!/usr/bin/python3
"""Defines a 'Square' class with a private instance attribute."""


class Square:
    """Definition of 'Square'"""
    def __init__(self, size=0):
        """Inits Square with a size integer.

        Args:
            size: An integer size of the square.

        Raises:
            TypeError: The size argument is not an integer.
            ValueError: The size argument is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Computes the area of the square."""
        return self.__size * self.__size

    @property
    def size(self):
        """Gets the size of the square

        Returns:
            The size attribute of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with a value

        Args:
            value: value to assign to size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints a square with '#'"""
        print("{}".format("\n".join(["#" * self.__size] * self.__size)))

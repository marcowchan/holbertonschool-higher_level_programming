#!/usr/bin/python3
"""Defines a 'Square' class with a private instance attribute."""


class Square:
    """Definition of 'Square'"""
    def __init__(self, size=0, position=(0, 0)):
        """Inits Square with a size integer.

        Args:
            size: An integer size of the square.
            position: A tuple of the position of the square.

        Raises:
            TypeError: Size is not an int or position is not a tuple of ints.
            ValueError: Size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if isinstance(position, tuple) and len(position) == 2 and\
            isinstance(position[0], int) and isinstance(position[1], int) and\
                position[0] >= 0 and position[1] >= 0:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Computes the area of the square."""
        return self.__size * self.__size

    @property
    def size(self):
        """Gets the size of the square.

        Returns:
            The size attribute of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with a value.

        Args:
            value: value to assign to size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints a square with '#'"""
        if self.__size == 0:
            print()
            return
        print("{}".format("\n" * self.__position[1]), end="")
        print("{}".format("\n".join(
            [" " * self.__position[0] + "#" * self.__size] * self.__size)))

    @property
    def position(self):
        """Gets the position of the square.

        Returns:
            Position of the Square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square

        Args:
            value: value to set the position
        """
        if isinstance(value, tuple) and len(value) == 2 and\
            isinstance(value[0], int) and isinstance(value[1], int) and\
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def __str__(self):
        """Returns a string similar to the one printed in my_print"""
        string = ""
        if self.__size == 0:
            return string
        string += "{}".format("\n" * self.__position[1])
        string += "{}".format("\n".join(
            [" " * self.__position[0] + "#" * self.__size] * self.__size))
        return string

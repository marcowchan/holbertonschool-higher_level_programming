#!/usr/bin/python3
"""Defines an Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """A base subclass with attributes for dimensions and position."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes dimensions and position attributes."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Validates and sets the width attribute."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Validates and sets the height attribute."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Validates and sets the x attribute."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Validates and sets the y attribute."""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Computes the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Prints a rectangle of '#'."""
        print("\n".join(["#" * self.width] * self.height))

#!/usr/bin/python3
"""Defines a Rectangle class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class with two private attributes: width and height."""
    def __init__(self, width, height):
        """Validates and sets width and height private attributes."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Computes the area of the Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a description of the rectangle."""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

#!/usr/bin/python3
"""Defines an Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """A base subclass with attributes for dimensions and position."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes dimensions and position attributes."""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

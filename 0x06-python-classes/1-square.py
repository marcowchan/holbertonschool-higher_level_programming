#!/usr/bin/python3
"""Defines a 'Square' class with a private instance attribute"""


class Square:
    """Definition of 'Square'"""
    def __init__(self, size=0):
        """Inits Square with 'size' private instance attribute"""
        self.__size = size

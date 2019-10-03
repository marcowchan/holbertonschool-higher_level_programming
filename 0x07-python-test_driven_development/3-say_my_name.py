#!/usr/bin/python3
"""Defines say_my_name function"""


def say_my_name(first_name, last_name=""):
    """Prints 'My name is <first name> <last name>'

    Args:
        first_name: A string containing the first name
        last_name: A string containing the last name
    Raises:
        TypeError: The first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

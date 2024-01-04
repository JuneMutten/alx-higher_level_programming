#!/usr/bin/python3

"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """
    Prints a name.
    Args:
        first_name (str): First name to be printed
        last_name (str): Last name to be printed
    Raises:
        TypeError: If either first_name or last_name are not strings
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

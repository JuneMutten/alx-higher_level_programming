#!/usr/bin/python3

"""Defines a text file-reading function."""


def append_write(filename="", text=""):
    """Prints a given number of lines from a text file"""

    with open(filename, 'a') as file:
        return file.write(text)

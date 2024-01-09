#!/usr/bin/python3

"""Defines a text file line-counting functio"""


def write_file(filename="", text=""):
    """Returns the number of lines in a text file"""
    with open(filename, 'w') as file:
        return file.write(text)

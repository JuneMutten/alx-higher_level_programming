#!/usr/bin/python3

"""Define a square class"""


class Square:
    """
    Square class with a private attribute size
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size

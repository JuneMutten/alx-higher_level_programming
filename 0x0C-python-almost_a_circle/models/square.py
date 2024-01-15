#!/usr/bin/python3

"""Defines a child class square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Module Representation of Square
    Args:
        size: size
        x: position
        y: position
        id: id
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialization a Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Module Square size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Module Square size setter
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Module string represation of square
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def update(self, *args, **kwargs):
        """m
        Mdule update square
        """
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.size = a
                elif i == 2:
                    self.x = a
                elif i == 3:
                    self.y = a
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """retrun dictonary
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

#!/usr/bin/python3
""" This is a square class"""


class Square:
    """ This is an empty class.

    Trying multiple ones
    """
    def __init__(self, size=0):
        """ Instantiate the instance with size """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.size = size

    def area(self):
        "Return the area of square"
        return self._Square__size ** 2

    @property
    def size(self):
        """get size property"""
        return self._Square__size

    @size.setter
    def size(self, value):
        """ Retrieve the size of a square and set it when value is provided"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = value

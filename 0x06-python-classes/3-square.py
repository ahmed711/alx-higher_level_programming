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

    def area(self):
        "Return the area of square"
        return self._Square__size ** 2

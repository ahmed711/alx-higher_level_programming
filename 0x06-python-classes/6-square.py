#!/usr/bin/python3
""" This is a square class"""


class Square:
    """ This is an empty class.

    Trying multiple ones
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Instantiate the instance with size """
        self.size = size
        self.position = position

    def area(self):
        "Return the area of square"
        return self.__size ** 2

    @property
    def size(self):
        """get size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Retrieve the size of a square and set it when value is provided"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        if not self.size:
            print()
        else:
            size = self.size
            [print() for i in range(self.position[1])]
            [print(" " * self.position[0] + "#" * size) for i in range(size)]

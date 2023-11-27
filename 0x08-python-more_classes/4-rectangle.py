#!/usr/bin/python3

"""
a rectangle class defined by its width and height

Rectangle(width, height)
"""


class Rectangle:
    """ Empty Rectangle Class"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        if (not self.__width or not self.__height):
            return ""
        return "\n".join(["#" * self.__width for i in range(self.__height)])

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if (not self.__width or not self.__height):
            return 0
        return ((self.__width + self.__height) * 2)

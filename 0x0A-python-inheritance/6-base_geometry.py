#!/usr/bin/python3
""" a class based on prev class """


BaseGeometry_5 = __import__('5-base_geometry').BaseGeometry


class BaseGeometry(BaseGeometry_5):
    """ a class based on prev class """
    def area(self):
        raise Exception("area() is not implemented")

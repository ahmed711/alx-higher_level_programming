#!/usr/bin/python3
""" a class based on prev class """


BaseGeometry_6 = __import__('6-base_geometry').BaseGeometry


class BaseGeometry(BaseGeometry_6):
    """ a class based on prev class """
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

#!/usr/bin/python3

"""
add_integar module is to add integars
input: integar or float
output: sum of the integar value of each number
"""


def add_integer(a, b=98):
    """ add two numbers
    if the inputs are not numbers a typeerror is raised
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

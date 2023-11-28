#!/usr/bin/python3
"""
Matric divisor

This function divides a matix by a number
"""


def matrix_divided(matrix, div):
    """ divide each cell in a matrix by a number """
    error_1 = "matrix must be a matrix (list of lists) of integers/floats"
    error_2 = "Each row of the matrix must have the same size"
    if not matrix or type(matrix) is not list:
        raise TypeError(error_1)
    if sum(list(map(lambda i: int(type(i) is list), matrix))) != len(matrix):
        raise TypeError(error_1)
    size = len(matrix[0])
    for ls in matrix:
        for i in ls:
            if type(i) not in [int, float]:
                raise TypeError(error_1)
    if sum(list(map(lambda i: int(len(i) == size), matrix))) != len(matrix):
        raise TypeError(error_2)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if not div:
        raise ZeroDivisionError("division by zero")
    new_mtrx = []
    for ls in matrix:
        new_mtrx.append([round(i/div, 2) for i in ls])
    return new_mtrx

#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and not len(matrix[0]):
        print("")
    for row in matrix:
        for i, num in enumerate(row):
            print("{:d}".format(num), end=" " if i != len(row) - 1 else "\n")

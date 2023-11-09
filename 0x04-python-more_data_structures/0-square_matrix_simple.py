#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = row[:]
        for i, num in enumerate(row):
            new_row[i] = num * num
        new_matrix.append(new_row)
    return new_matrix

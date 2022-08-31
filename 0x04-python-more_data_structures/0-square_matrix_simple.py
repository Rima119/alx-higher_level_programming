#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        new_matrix = []
        for n in matrix:
            new_matrix.append(list(map(lambda x: x*x, n)))
        return new_matrix

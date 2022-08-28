#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for n in matrix:
        for m in range(len(n)):
            if (m < (len(matrix[n])) - 1):
                print("{:d}".format(matrix[n][m]), end=' ')
            else:
                print("{:d}".format(matrix[n][m]), end='')
        print()

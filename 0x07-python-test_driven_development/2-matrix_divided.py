#!/usr/bin/python3
"""matrix_divided module"""



def matrix_divided(matrix, div):
    """function that divides all elements of a matrix

    Args:
        matrix: list of lists of integers or floats
        div: number
    
    Returns:
           returns a new matrix
    """
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    a = 0
    for n in matrix:
        if type(n) != list:
            raise TypeError("Each row of the matrix must have the same size")
        if a != 0 and len(n) != a:
            raise TypeError("Each row of the matrix must have the same size")
        for m in n:
            if type(m) != int and type(m) != float:
                raise TypeError("Each row of the matrix must have the same size")
        a = len(n)
    return list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))

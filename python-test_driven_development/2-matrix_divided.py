#!/usr/bin/python3
"""A function for dived a matrix
"""


def matrix_divided(matrix, div):
    """Divide a matrix with this function
    """
    matrixerror = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(matrixerror)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(matrixerror)
        for item in row:
            if not isinstance(item, (float, int)):
                raise TypeError(matrixerror)
    for i in range(len(matrix) - 1):
        if len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    try:
        return [list(map((lambda x: round(x / div, 2)), i)) for i in matrix]
    except ZeroDivisionError:
        raise ZeroDivisionError("division by zero")

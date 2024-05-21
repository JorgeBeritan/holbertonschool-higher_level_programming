#!/usr/bin/python3


def matrix_divided(matrix, div):
    """Divide a matrix with this function
    """
    if not matrix  or not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for item in row:
            if not isinstance(item, (float, int)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in range(len(matrix) - 1):
        if len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    try:
        return [list(map((lambda x: round(x / div, 2)), i)) for i in matrix]
    except ZeroDivisionError:
        raise ZeroDivisionError("division by zero")

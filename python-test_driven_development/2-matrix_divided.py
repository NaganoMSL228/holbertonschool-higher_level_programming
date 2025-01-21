#!/usr/bin/python3


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given number"""
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(matrix[0]) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return [[round(element / div, 2) for element in row] for row in matrix]

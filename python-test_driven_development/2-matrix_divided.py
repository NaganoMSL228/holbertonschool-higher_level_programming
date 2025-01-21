#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.
    
    Args:
        matrix (list of lists): A matrix of integers/floats.
        div (int/float): A non-zero integer or float to divide by.

    Returns:
        list of lists: New matrix with elements divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix elements are not integers/floats,
                   or if matrix rows aren't all the same size,
                   or if div is not an integer/float.
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    return [[round(element / div, 2) for element in row] for row in matrix]

#!/usr/bin/python3
"""Defines matrix_divided"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix: A list of lists of integers or floats.
        div: The divisor to divide the elements of the matrix by.
    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats.
            or the rows of the matrix are not of the same size
            or div is not a integer or a float
        ZeroDivisionError: If div is zero
    Returns:
        A new matrix of quotients
    """
    invalid_mat = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(invalid_mat)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_len = None
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(invalid_mat)
        if row_len is not None and row_len != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        row_len = len(row)
        for col in row:
            if not isinstance(col, int) and not isinstance(col, float):
                raise TypeError(invalid_mat)

    return [[round(col / div, 2) for col in row] for row in matrix]

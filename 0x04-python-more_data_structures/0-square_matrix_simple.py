#!/usr/bin/python3
def square_all(element):
    if isinstance(element, list):
        return list(map(square_all, element))
    return (element * element)


def square_matrix_simple(matrix=[]):
    return list(map(square_all, matrix))

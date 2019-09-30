#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    cols = len(matrix[0])
    if cols == 0:
        print()
        return
    for i in range(rows):
        delim = ' '
        for j in range(cols):
            if j == cols - 1:
                delim = '\n'
            print("{:d}".format(matrix[i][j]), end=delim)

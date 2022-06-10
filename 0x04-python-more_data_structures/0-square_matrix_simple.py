#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        row = []
        new_matrix.append(row)
        for j in range(len(matrix[i])):
            element = matrix[i][j] ** 2
            row.append(element)
    return new_matrix

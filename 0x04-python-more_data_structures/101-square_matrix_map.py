#!/usr/bin/python3

#a function that computes the square value of all integers of a matrix using map
def square_matrix_map(matrix=[]):
    return list(map(lambda row: list(map(lambda x: x**2, row)), matrix))

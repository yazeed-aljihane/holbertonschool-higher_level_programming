#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == matrix[i][-1]:
                print("{:d}".format(matrix[i][j]), end="\n")
                break
            print("{:d}".format(matrix[i][j]), end=" ")

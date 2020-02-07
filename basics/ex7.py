#!/bin/python3.6
def diagonalReverse(matrix):
	x = len(matrix[0])
	y = len(matrix)
	new_matrix = list()
	for i in range(y):
		new_matrix.append(list(range(x)))
	for i in range(x):
		for j in range(y):
			new_matrix[j][i] = matrix[i][j]
	return new_matrix

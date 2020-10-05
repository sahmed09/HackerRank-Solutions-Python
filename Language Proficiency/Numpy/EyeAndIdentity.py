import numpy

row, col = map(int, input().split())

# print(numpy.eye(row, col, k=0,))

numpy.set_printoptions(sign=" ")  # for internal extra spacing
print(numpy.eye(row, col, k=0))  # k=0 for main diagonal
# print(numpy.eye(*map(int, input().split())))  # same as previous

# print(numpy.eye(row, col, k=1))  # k=1 or any positive k for upper diagonal
# print(numpy.eye(row, col, k=-1))  # k=-1 or any negative k for lower diagonal

# print(numpy.identity(row))

"""identity:
The identity tool returns an identity array. An identity array is a square matrix with all the 
main diagonal elements as 1 and the rest as 0. The default type of elements is float.
print(numpy.identity(3))

eye:
The eye tool returns a 2-D array with 1's as the diagonal and 0's elsewhere. The diagonal can be main,
upper or lower depending on the optional parameter k. A positive k is for the upper diagonal, 
a negative k is for the lower, and a 0 k (default) is for the main diagonal.
print(numpy.eye(8, 7, k = 1))  # 8 X 7 Dimensional array with first upper diagonal 1.
print(numpy.eye(8, 7, k = -2))  # 8 X 7 Dimensional array with second lower diagonal 1."""

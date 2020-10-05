import numpy

# The linalg.det tool computes the determinant of an array.
n = int(input())

my_array = numpy.array([input().strip().split() for _ in range(n)], float)

numpy.set_printoptions(legacy="1.13")
determinant = numpy.linalg.det(my_array)

print(determinant)

# The linalg.eig computes the eigenvalues and right eigenvectors of a square array.
# vals, vecs = numpy.linalg.eig([[1, 2], [2, 1]])
# print(vals)
# print(vecs)

# The linalg.inv tool computes the (multiplicative) inverse of a matrix.
# print(numpy.linalg.inv([[1, 2], [2, 1]]))

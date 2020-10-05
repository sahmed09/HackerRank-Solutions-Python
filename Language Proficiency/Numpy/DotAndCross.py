import numpy

n = int(input())

A = numpy.array([input().strip().split() for _ in range(n)], int)
B = numpy.array([input().strip().split() for _ in range(n)], int)

prod = numpy.dot(A, B)
print(prod)

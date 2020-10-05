import numpy

shape = list(map(int, input().split()))
# print(n, m, k)

print(numpy.zeros(shape, dtype=numpy.int))
print(numpy.ones(shape, dtype=numpy.int))

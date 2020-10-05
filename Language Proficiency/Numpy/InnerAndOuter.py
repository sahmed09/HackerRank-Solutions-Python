import numpy

A = numpy.array(input().strip().split(), int)
B = numpy.array(input().strip().split(), int)

print(numpy.inner(A, B))
print(numpy.outer(A, B))

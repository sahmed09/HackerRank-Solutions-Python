import numpy

P = numpy.array(input().strip().split(), float)
x = float(input())

print(numpy.polyval(P, x))

import numpy

n, m = map(int, input().split())

my_array = numpy.array([input().strip().split() for _ in range(n)], int)

# minimum = numpy.min(my_array, axis=1)
# maximum = numpy.max(minimum, axis=None)

maximum = numpy.max(numpy.min(my_array, axis=1), axis=None)

print(maximum)

import numpy

n, m = map(int, input().split())

numpy.set_printoptions(legacy='1.13')
# It tells the numpy print formatter to use the default settings from numpy version 1.13 instead of
# numpy current version
my_array = numpy.array([input().strip().split() for _ in range(n)], int)

mean = numpy.mean(my_array, axis=1)
var = numpy.var(my_array, axis=0)
std = numpy.std(my_array, axis=None)

print(mean)
print(var)
print(std)

import numpy


def arrays(arr):
    return numpy.array(arr, float)[::-1]


arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# From Editorial:
print(numpy.flipud(numpy.array(input().split(), float)))

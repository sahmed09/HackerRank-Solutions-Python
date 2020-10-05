import numpy

n, m = map(int, input().split())

my_array = numpy.array([input().strip().split() for _ in range(n)], int)

# summation = numpy.sum(my_array, axis=0)
# prod = numpy.prod(summation, axis=None)

prod = numpy.prod(numpy.sum(my_array, axis=0), axis=None)

print(prod)

"""sum:
The sum tool returns the sum of array elements over a given axis. By default, the axis value is None.

my_array = numpy.array([ [1, 2], [3, 4] ])
print(numpy.sum(my_array, axis = 0))  # Output : [4 6]
print(numpy.sum(my_array, axis = 1))  # Output : [3 7]
print(numpy.sum(my_array, axis = None))  # Output : 10
print(numpy.sum(my_array))  # Output : 10

prod:
The prod tool returns the product of array elements over a given axis. By default, the axis value is None.

my_array = numpy.array([ [1, 2], [3, 4] ])
print(numpy.prod(my_array, axis = 0))  # Output : [3 8]
print(numpy.prod(my_array, axis = 1))  # Output : [ 2 12]
print(numpy.prod(my_array, axis = None))  # Output : 24
print(numpy.prod(my_array))  # Output : 24
"""

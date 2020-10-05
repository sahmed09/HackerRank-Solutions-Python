import numpy

arr = input().strip().split(' ')

print(numpy.reshape(numpy.array(arr, int), (3, 3)))  # Default type is float

# new_arr = numpy.reshape(numpy.array(arr, int), (3, 3))
# print(new_arr)
# print(new_arr.shape)

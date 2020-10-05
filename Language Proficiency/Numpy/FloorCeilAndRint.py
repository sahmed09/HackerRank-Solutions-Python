import numpy

my_array = numpy.array(input().split(), float)

numpy.set_printoptions(sign=" ")
print(numpy.floor(my_array))
print(numpy.ceil(my_array))
print(numpy.rint(my_array))

"""floor:
The tool floor returns the floor of the input element-wise.
The floor of x is the largest integer i where i<=x
numpy.floor(my_array)
ceil:
The tool ceil returns the ceil of the input element-wise.
The ceil of x is the smallest integer i where i>=x
numpy.ceil(my_array)
rint:
The rint tool rounds to the nearest integer of input element-wise.
numpy.rint(my_array)"""

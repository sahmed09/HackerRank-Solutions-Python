import numpy

row, col = map(int, input().split())

arr = []

for i in range(row):
    inp = numpy.array(input().split(), int)
    arr.append(inp)

new_arr = numpy.array(arr)
print(numpy.transpose(new_arr))
print(new_arr.flatten())

# Another Approach:
n, m = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(n)], int)
print(array.transpose())
print(array.flatten())

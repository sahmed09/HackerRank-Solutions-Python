import re
n = int(input())

binary = "{0:b}".format(n)
# print(binary)
ones = binary.split("0")
# ones = re.split("0+", binary)
# print(ones)
print(len(max(ones)))

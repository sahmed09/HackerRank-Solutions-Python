from itertools import *

inp = input()

for i, j in groupby(inp):
    print(tuple([len(list(j)), int(i)]), end=" ")

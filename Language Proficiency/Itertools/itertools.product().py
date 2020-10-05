from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = list(product(A, B))
# print(result)

for item in result:
    print(item, end=" ")

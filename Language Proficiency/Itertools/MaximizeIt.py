from itertools import product

k, m = map(int, input().split())

n = []
for i in range(k):
    n.append(list(map(int, input().split()))[1:])
prod = list(product(*n))
# print(prod)

result = []
for combination in prod:
    total = 0
    for i in combination:
        total += i**2
    result.append(total % m)

print(max(result))

# Using lambda:
K, M = map(int, input().split())
N = []

for _ in range(K):
    N.append(list(map(int, input().split()))[1:])
MAX = -1
for i in product(*N):
    MAX = max(sum(map(lambda x: x ** 2, i)) % M, MAX)

print(MAX)

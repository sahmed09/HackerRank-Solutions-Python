from collections import Counter

# A counter is a container that stores elements as dictionary keys, and their counts are stored as
# dictionary values.

X = input()
S = Counter(map(int, input().split()))
# print(S)

earnings = 0
for customer in range(int(input())):
    size, x_i = map(int, input().split())
    if size in S and S[size] > 0:
        # print(S[size])
        S[size] -= 1
        earnings += x_i

print(earnings)

# Normal Approach:
"""n = int(input())
lis = list(map(int, input().strip().split()))
# print(Counter(lis))
# print(lis)
total = 0

for _ in range(int(input())):
    size, price = map(int, input().split())
    if size in lis:
        lis.remove(size)
        total += price

print(total)"""

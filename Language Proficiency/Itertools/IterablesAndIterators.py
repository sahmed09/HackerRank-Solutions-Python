from itertools import combinations

N = int(input())
number = list(input().split())
K = int(input())

combination = list(combinations(number, K))

count = 0
for i in combination:
    if "a" in i:
        count += 1

print(count/len(combination))
# print("{0:.3}".format(count/len(combination)))

from itertools import combinations

word, size = input().split(' ')
size = int(size)

for i in range(1, size+1):
    for j in list(combinations(sorted(word), i)):
        print("".join(j))

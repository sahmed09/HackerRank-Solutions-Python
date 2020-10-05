from itertools import combinations_with_replacement

word, size = input().split(' ')

for i in list(combinations_with_replacement(sorted(word), int(size))):
    print("".join(i))

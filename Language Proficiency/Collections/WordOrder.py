from collections import Counter

words = []

for i in range(int(input())):
    words.append(input().strip())

counts = Counter(words)

print(len(counts))
print(*counts.values())

# for i in counts.values():
#     print(i, end=" ")

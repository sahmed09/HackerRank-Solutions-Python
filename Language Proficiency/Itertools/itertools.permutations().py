from itertools import permutations

word, size = input().split(' ')

for i in list(permutations(sorted(word), int(size))):
    print("".join(i))

# result = list(permutations(word, int(size)))
# result.sort()
# # print(result)
#
# for item in result:
#     print("".join(item))

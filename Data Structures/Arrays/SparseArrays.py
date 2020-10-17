from collections import Counter


def matchingStrings(strings, queries):
    counter = Counter(strings)
    result = []
    for word in queries:
        result.append(counter[word])
    return result


if __name__ == '__main__':
    strings_count = int(input())
    strings = []
    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())
    queries = []
    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)
    print(res)


# Using only Dictionary:
# def matchingStrings(strings, queries):
#     words = dict()
#     ans = []
#     for w in strings:
#         if w in words:
#             words[w] += 1
#         else:
#             words[w] = 1
#     for q in queries:
#         if q in words:
#             ans.append(words[q])
#         else:
#             ans.append(0)
#     return ans

# Using DefaultDict:
# from collections import defaultdict
# def matchingStrings(strings, queries):
#     words = defaultdict(lambda: 0)
#
#     for word in strings:
#         words[word] += 1
#     # print(words.items())
#
#     result = []
#     for word in queries:
#         result.append(words[word])
#     return result

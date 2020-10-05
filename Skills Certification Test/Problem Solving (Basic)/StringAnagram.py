from collections import Counter


def stringAnagram(dictionary, query):
    dictionary = ["".join(sorted(i)) for i in dictionary]
    query = ["".join(sorted(i)) for i in query]
    counter = Counter(dictionary)
    result = []
    for i in query:
        if i in counter:
            result.append(counter[i])
        else:
            result.append(0)
    return result


if __name__ == '__main__':
    dictionary_count = int(input().strip())
    dictionary = []
    for _ in range(dictionary_count):
        dictionary_item = input()
        dictionary.append(dictionary_item)

    query_count = int(input().strip())
    query = []
    for _ in range(query_count):
        query_item = input()
        query.append(query_item)

    result = stringAnagram(dictionary, query)
    print(result)

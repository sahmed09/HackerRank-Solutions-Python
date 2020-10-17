def arrayManipulation(n, queries):
    array = [0] * (n+1)

    for query in queries:
        a = query[0]
        b = query[1]
        k = query[2]
        array[a] += k
        if (b + 1) <= n:
            array[b+1] -= k

    max_value = 0
    running_count = 0
    for i in range(1, n+1):
        running_count += array[i]
        if max_value < running_count:
            max_value = running_count
    return max_value
# Time Complexity: O(m logm)


# def arrayManipulation(n, queries):
#     arr = [0] * (n+1)
#     # add the value at first index
#     # subtract the value at last index + 1
#     for q in queries:
#         start, end, amt = q
#         arr[start-1] += amt
#         arr[end] -= amt
#
#     # max value and running sum
#     mv = -1
#     running = 0
#     for a in arr:
#         running += a
#         if running > mv:
#             mv = running
#
#     return mv


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)

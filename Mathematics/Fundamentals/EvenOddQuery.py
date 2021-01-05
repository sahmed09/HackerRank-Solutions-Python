def solve(arr, queries):
    result = []
    for a, b in queries:
        if a != b and arr[a] == 0:
            result.append("Odd")
        elif arr[a-1] % 2 == 0:
            result.append("Even")
        else:
            result.append("Odd")
    return result


# def solve(arr, queries):
#     result = []
#     for a, b in queries:
#         if a < len(arr) and arr[a] == 0 and a != b:
#             result.append('Odd')
#         else:
#             if arr[a-1] % 2 == 0:
#                 result.append("Even")
#             else:
#                 result.append("Odd")
#     return result


if __name__ == '__main__':
    arr_count = int(input())
    arr = list(map(int, input().rstrip().split()))

    q = int(input())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = solve(arr, queries)
    print(result)

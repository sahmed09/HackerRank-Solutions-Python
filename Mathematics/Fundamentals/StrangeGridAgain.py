def strangeGrid(r, c):
    if r % 2 == 0:
        result = 2 * (c - 1) + 1 + 5 * (r - 2)
    else:
        result = 2 * (c - 1) + 5 * (r - 1)
    return result
# Time Complexity: O(1)


# From editorial:
# def strangeGrid(r, c):
#     if r % 2 == 1:
#         r = r // 2
#         answer = 10 * r + 2 * (c - 1)
#     else:
#         r = (r - 1) // 2
#         answer = 10 * r + 2 * (c - 1) + 1
#     return answer


if __name__ == '__main__':
    rc = input().split()
    r = int(rc[0])
    c = int(rc[1])

    result = strangeGrid(r, c)
    print(result)

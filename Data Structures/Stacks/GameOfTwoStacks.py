def twoStacks(x, a, b):
    a.reverse()
    b.reverse()
    stack = []
    total, score = 0, 0

    while a:
        item = a.pop()
        if (total + item) <= x:
            total += item
            score += 1
            stack.append(item)
        else:
            break

    max_score = score

    while b:
        # print("b ", b)
        item = b.pop()
        # print("item ", item)
        total += item
        score += 1
        while total > x and stack:
            total -= stack.pop()
            # print("total ", total)
            score -= 1
            # print("score ", score)
        if total <= x and score > max_score:
            max_score = score
            # print("max ", max_score)

    return max_score


# def twoStacks(x, a, b):
#     total, count, i, j = 0, 0, 0, 0
#
#     while i < len(a) and total + a[i] <= x:  # considering only first stack and calculating count
#         total += a[i]
#         i += 1
#
#     count = i
#
#     while j < m and i >= 0:  # now adding one element of second stack at a time and subtracting the top element of
#         # first stack and calculating the count
#         total += b[j]
#         j += 1
#         while total > x and i > 0:
#             i -= 1
#             total -= a[i]
#         if total <= x and i + j > count:
#             count = i + j
#
#     return count


if __name__ == '__main__':
    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])
        m = int(nmx[1])
        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))
        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)
        print(result)

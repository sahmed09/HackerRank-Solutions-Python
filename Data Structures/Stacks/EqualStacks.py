# def equalStacks(h1, h2, h3):
#     sum1, sum2, sum3 = map(sum, (h1, h2, h3))
#     while h1 and h2 and h3:
#         minimum = min(sum1, sum2, sum3)
#         while sum1 > minimum:
#             sum1 -= h1.pop(0)
#         while sum2 > minimum:
#             sum2 -= h2.pop(0)
#         while sum3 > minimum:
#             sum3 -= h3.pop(0)
#         if sum1 == sum2 == sum3:
#             return sum1
#     return 0


def equalStacks(h1, h2, h3):
    h1 = h1[::-1]
    h2 = h2[::-1]
    h3 = h3[::-1]

    sum_h1 = sum(h1)
    sum_h2 = sum(h2)
    sum_h3 = sum(h3)

    while not sum_h1 == sum_h2 == sum_h3:
        if sum_h1 > sum_h2 or sum_h1 > sum_h3:
            t = h1.pop()
            sum_h1 -= t
        if sum_h2 > sum_h1 or sum_h2 > sum_h3:
            t = h2.pop()
            sum_h2 -= t
        if sum_h3 > sum_h1 or sum_h3 > sum_h2:
            t = h3.pop()
            sum_h3 -= t

    return sum_h1


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])
    n2 = int(first_multiple_input[1])
    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))
    h2 = list(map(int, input().rstrip().split()))
    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)
    print(result)

import math


def solve(n):
    result = (-1 + math.sqrt(1 + 8 * n)) / 2
    if result == int(result):
        return "Go On Bob " + str(int(result))
    else:
        return "Better Luck Next Time"


# def solve(n):
#     result = int((-1 + math.sqrt(1 + 8 * n)) / 2)
#     if n == (result * (result + 1)) // 2:
#         return "Go On Bob " + str(int(result))
#     else:
#         return "Better Luck Next Time"


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)
        print(result)

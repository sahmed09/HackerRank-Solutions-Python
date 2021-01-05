import math


def gameWithCells(n, m):
    return math.ceil(n / 2) * math.ceil(m / 2)
    # return ((n + 1) // 2) * ((m + 1) // 2)


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])
    m = int(nm[1])

    result = gameWithCells(n, m)
    print(result)

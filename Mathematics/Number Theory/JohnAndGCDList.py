import math


def solve(a):
    res = []
    temp = a[0]
    for item in a:
        res.append((temp*item) // math.gcd(temp,item))
        temp = item
    res.append(a[-1])
    return res


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        a_count = int(input())
        a = list(map(int, input().rstrip().split()))

        result = solve(a)
        print(*result)

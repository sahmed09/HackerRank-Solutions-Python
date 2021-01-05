def solve(a, b):
    a, b = int(a), int(b)
    mod = 10 ** 9 + 7
    b = b % (mod - 1)
    return pow(a, b, mod)

# def solve(a, b):
#     a, b = int(a), int(b)
#     m = 10 ** 9 + 7
#     return pow(a, b, m)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        ab = input().split()

        a = ab[0]

        b = ab[1]

        result = solve(a, b)
        print(result)

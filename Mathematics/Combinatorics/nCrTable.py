from math import factorial


def solve(n):
    result = []
    for i in range(n+1):
        ncr = (factorial(n) // factorial(i) // factorial(n-i)) % 10**9
        result.append(ncr)
    return result


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)
        print(*result)

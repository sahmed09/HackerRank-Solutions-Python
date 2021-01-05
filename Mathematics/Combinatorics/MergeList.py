from math import factorial


def solve(n, m):
    return (factorial(n + m) // factorial(n) // factorial(m)) % (10 ** 9 + 7)
# Time Complexity: O(N+M)
# Formula: ((n+m)! // (n! * m!)) % (10 ** 9 + 7)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = solve(n, m)
        print(result)

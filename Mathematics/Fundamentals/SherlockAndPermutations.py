from math import factorial


# We fix a 1 at the first position. Now we are left with M-1 1s and N 0s. Now we can just count unique permutations
# of (M-1) 1s and N 0s, which is choose((M+N-1), N), which is (M+N-1)!/(N! * (M-1)!).
def solve(n, m):
    return (factorial(n + m - 1) // factorial(n) // factorial(m - 1)) % (10 ** 9 + 7)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = solve(n, m)
        print(result)

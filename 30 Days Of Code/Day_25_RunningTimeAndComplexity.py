import math


def isPrime(n):
    if n == 2:
        return True
    elif n == 1 or (n & 1) == 0:
        return False

    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False

    return True


p = int(input())
for i in range(0, p):
    x = int(input())

    s = "Prime" if (isPrime(x)) else "Not prime"
    print(s)
    # Time complexity : O(n^(1/2))


"""def isPrime(n):
    p = 2
    while p*p <= n:
        if n % p == 0:
            n = 1
            break
        p += 1

    if n == 0 or n == 1:
        print("Not prime")
    else:
        print("Prime")


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        isPrime(n)"""

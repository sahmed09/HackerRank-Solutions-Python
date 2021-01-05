import os


def connectingTowns(n, routes):
    count = 1
    for i in routes:
        count *= i
        count %= 1234567
    return count
    # (a*b) mod M = ((a mod M) * (b mod M)) mod M
    # Time Complexity: O(n)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        routes = list(map(int, input().rstrip().split()))
        result = connectingTowns(n, routes)
        print(result)

        # fptr.write(str(result) + '\n')
    # fptr.close()

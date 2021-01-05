import os


def solve(n, m):
    return (n * m) - 1  # Time Complexity: O(1)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    result = solve(n, m)
    print(result)

    # fptr.write(str(result) + '\n')
    # fptr.close()

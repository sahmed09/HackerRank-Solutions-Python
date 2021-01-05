import os


def solve(n, operations):
    total = 0
    for item in operations:
        total = total + ((item[1]-item[0]) + 1) * item[2]
    return total//n
    # return int(sum([(o[1] - o[0] + 1) * o[2] for o in operations]) / n)  # Single Line Approach


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])
    m = int(nm[1])

    operations = []
    for _ in range(m):
        operations.append(list(map(int, input().rstrip().split())))

    result = solve(n, operations)
    print(result)

    # fptr.write(str(result) + '\n')
    # fptr.close()

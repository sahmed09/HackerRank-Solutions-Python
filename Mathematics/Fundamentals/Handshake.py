import os


def handshake(n):
    return (n * (n - 1)) // 2


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = handshake(n)
        print(result)

        # fptr.write(str(result) + '\n')
    # fptr.close()

# Time complexity: O(1)
# nC2 = (n*(n-1))/2

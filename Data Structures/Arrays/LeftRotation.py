def rotateLeft(d, arr):
    return arr[d:] + arr[:d]
    # shifted = arr[d % len(arr):] + arr[:d % len(arr)]
    # return shifted


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)
    print(*result)

def reverseArray(a):
    return a[::-1]


if __name__ == '__main__':
    arr_count = int(input())
    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)
    print(res)
    # Time Complexity: O(n)

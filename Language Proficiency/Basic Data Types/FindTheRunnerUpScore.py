if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    a = max(arr)

    c = arr.count(a)

    for i in range(c):
        arr.remove(a)
    print(max(arr))

    # n = int(input())
    # arr = list(map(int, input().split()))
    # print(arr)
    # arr.sort(reverse=True)
    # print(arr)
    # pos = arr[0]
    # for i in range(len(arr)):
    #     if arr[i+1] < pos:
    #         pos = arr[i+1]
    #         break
    #     else:
    #         continue
    # print(pos)

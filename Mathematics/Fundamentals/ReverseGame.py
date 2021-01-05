if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])

        # if k < n - 1 - k:
        #     print(2 * k + 1)
        # else:
        #     print(2 * (n - 1 - k))

        if k < n // 2:
            print(2 * k + 1)
        else:
            print(2 * (n - 1 - k))

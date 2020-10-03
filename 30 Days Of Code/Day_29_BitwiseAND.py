if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])

        print(k-1 if ((k-1) | k) <= n else k-2)
        # 5 8 -> 6 -- 7|8 = 0111|1000 = 1111 = 15 > 5 -> result = k-2 = 8-2 = 6
        # 9 6 -> 5 -- 5|6 = 101|110 = 111 = 7 < 9 -> result = k-1 = 6-1 = 5
    # print(~t)

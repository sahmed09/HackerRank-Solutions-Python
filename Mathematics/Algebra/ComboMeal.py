def profit(b, s, c):
    return b + s - c


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        bsc = input().split()
        b = int(bsc[0])
        s = int(bsc[1])
        c = int(bsc[2])

        result = profit(b, s, c)
        print(result)

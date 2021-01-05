def solve(n):
    i = 1
    while True:
        binary = int("{0:b}".format(i).replace('1', '9'))
        # binary = int(bin(i)[2:].replace('1', '9'))
        if binary % n == 0:
            break
        i += 1
    return str(binary)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)
        print(result)

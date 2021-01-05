def lights(n):
    return (pow(2, n) - 1) % 100000


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = lights(n)
        print(result)

cube = lambda x: pow(x, 3)  # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers
    lists = [0, 1]
    for i in range(2, n):
        lists.append(lists[i - 2] + lists[i - 1])
    return lists[:n]


if __name__ == '__main__':
    n = int(input())
    # print(fibonacci(n))
    print(list(map(cube, fibonacci(n))))


"""def fibonacci(n):
    # return a list of fibonacci numbers
    first = 0
    sec = 1
    lists = []
    if n == 0:
        lists = lists
    elif n == 1:
        lists.append(first)
    elif n == 2:
        lists = [first, sec]
    else:
        lists = [first, sec]
        for i in range(3, n + 1):
            fib = first + sec
            lists.append(fib)
            first = sec
            sec = fib
    return lists"""

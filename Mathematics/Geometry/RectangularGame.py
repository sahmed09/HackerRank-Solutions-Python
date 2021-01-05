def solve(steps):
    x = []
    y = []
    for step in steps:
        x.append(step[0])
        y.append(step[1])
    return min(x) * min(y)


if __name__ == '__main__':
    n = int(input())

    steps = []

    for _ in range(n):
        steps.append(list(map(int, input().rstrip().split())))

    result = solve(steps)
    print(result)

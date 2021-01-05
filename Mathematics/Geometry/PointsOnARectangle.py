def solve(coordinates):
    x = []
    y = []
    for coordinate in coordinates:
        x.append(coordinate[0])
        y.append(coordinate[1])

    count = 0
    for coordinate in coordinates:
        if min(x) < coordinate[0] < max(x) or min(y) < coordinate[1] < max(y):
            count += 1

    if count > 0:
        return "NO"
    else:
        return "YES"
# Time Complexity: O(N)


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        n = int(input())

        coordinates = []

        for _ in range(n):
            coordinates.append(list(map(int, input().rstrip().split())))

        result = solve(coordinates)
        print(result)

def solve(coordinates):
    max_x, max_y, min_x, min_y = 0, 0, 0, 0  # all are zero at beginning

    for coordinate in coordinates:
        x, y = coordinate[0], coordinate[1]
        if max_x < x:
            max_x = x
        if max_y < y:
            max_y = y
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y

    maximum = []
    # we need to calculate the max of all possible knowing there is a zero in each point
    maximum.append(max_x - min_x)  # if min_y & max_y both zero
    maximum.append(max_y - min_y)  # if min_x & max_x both zero
    maximum.append((max_x ** 2 + max_y ** 2) ** 0.5)  # if min_x & min_y are zero
    maximum.append((max_x ** 2 + min_y ** 2) ** 0.5)  # if min_x & max_y are zero
    maximum.append((min_x ** 2 + max_y ** 2) ** 0.5)  # if max_x & min_y are zero
    maximum.append((min_x ** 2 + min_y ** 2) ** 0.5)  # if max_x & max_y are zero
    return "%.6f" % max(maximum)


if __name__ == '__main__':
    n = int(input())

    coordinates = []

    for _ in range(n):
        coordinates.append(list(map(int, input().rstrip().split())))

    result = solve(coordinates)
    print(result)

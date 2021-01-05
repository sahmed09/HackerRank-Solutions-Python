def solve(points):
    if points[0][0] == points[1][0] == points[2][0] == points[3][0] or points[0][1] == points[1][1] == points[2][1] \
           == points[3][1] or points[0][2] == points[1][2] == points[2][2] == points[3][2]:
        return "YES"
    else:
        return "NO"
# Time Complexity: O(1)


# def solve(points):
#     set_a = set()
#     set_b = set()
#     set_c = set()
#
#     for point in points:
#         set_a.add(point[0])
#         set_b.add(point[1])
#         set_c.add(point[2])
#
#     if len(set_a) == 1 or len(set_b) == 1 or len(set_c) == 1:
#         return "YES"
#     else:
#         return "NO"


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        points = []

        for _ in range(4):
            points.append(list(map(int, input().rstrip().split())))

        result = solve(points)
        print(result)

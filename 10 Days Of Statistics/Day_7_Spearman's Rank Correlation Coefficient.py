def get_rank(data):
    temp = sorted(data)
    rank = dict()
    for i in range(len(temp)):
        rank[temp[i]] = i + 1
    return [rank[i] for i in data]


n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

rx = get_rank(X)
ry = get_rank(Y)

d = [(rx[i] - ry[i]) ** 2 for i in range(n)]
rxy = 1 - ((6 * sum(d)) / (n * (n ** 2 - 1)))

print(round(rxy, 3))

# Another Approach:
# def get_rank(data):
#     x_rank = dict((x, i+1) for i, x in enumerate(sorted(set(data))))
#     return [x_rank[x] for x in data]
#
#
# n = int(input())
# X = list(map(float, input().split()))
# Y = list(map(float, input().split()))
#
# rx = get_rank(X)
# ry = get_rank(Y)
#
# d = [(rx[i] - ry[i]) ** 2 for i in range(n)]
# rxy = 1 - ((6 * sum(d)) / (n * (n ** 2 - 1)))
#
# print(round(rxy, 3))

# Another Approach:
# n = int(input())
# x = [float(i) for i in input().strip().split()]
# y = [float(i) for i in input().strip().split()]
#
# rx = [sorted(x).index(i) for i in x]
# ry = [sorted(y).index(i) for i in y]
#
# rxy =1-(sum([(rx[i]-ry[i])**2 for i in range(n)])*6/(n*(n**2-1)))
# print(round(rxy, 3))

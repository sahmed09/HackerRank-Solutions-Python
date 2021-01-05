if __name__ == '__main__':
    n = int(input())

    x_axis = set()
    y_axis = set()

    for n_itr in range(n):
        xy = input().split()
        x = int(xy[0])
        y = int(xy[1])
        x_axis.add(x)
        y_axis.add(y)

    if len(x_axis) == 1 or len(y_axis) == 1:
        print("YES")
    else:
        print("NO")

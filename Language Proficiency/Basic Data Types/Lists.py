if __name__ == '__main__':
    N = int(input())
    # N = 12

    lists = []
    while N > 0:
        inp = [x for x in input().split(' ')]
        if inp[0] == "insert":
            lists.insert(int(inp[1]), int(inp[2]))
        elif inp[0] == "append":
            lists.append(int(inp[1]))
        elif inp[0] == "remove":
            lists.remove(int(inp[1]))
        elif inp[0] == "pop":
            lists.pop()
        elif inp[0] == "sort":
            lists.sort()
        elif inp[0] == "reverse":
            lists.reverse()
        elif inp[0] == "print":
            print(lists)
        N = N - 1

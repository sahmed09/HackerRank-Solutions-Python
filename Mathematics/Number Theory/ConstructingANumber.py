def canConstruct(a):
    result = sum(a)
    if result % 3 == 0:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        a = list(map(int, input().rstrip().split()))

        result = canConstruct(a)
        print(result)

        # Time Complexity: O(N)

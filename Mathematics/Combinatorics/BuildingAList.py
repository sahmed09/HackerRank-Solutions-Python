from itertools import combinations


# def solve(s):
#     size = len(s)
#     word = []
#     for i in range(1, size + 1):
#         for j in list(combinations(s, i)):
#             word.append("".join(j))
#     return sorted(word)


# Without itertools
def solve(s):
    size = len(s)
    word = []
    for i in range(1, 2**size):
        test = str(bin(i))[2:][::-1]
        out = ""
        for i in range(0, len(test)):
            if test[i] == '1':
                out = out + str(s[i])
        word.append(out)
    return sorted(word)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        s = input()

        result = solve(s)

        print(*result, sep="\n")

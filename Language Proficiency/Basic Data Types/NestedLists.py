if __name__ == '__main__':
    marksheet = []
    scoresheet = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet += [[name, score]]
        scoresheet += [score]

    x = sorted(set(scoresheet))[1]

    for n, s in sorted(marksheet):
        if s == x:
            print(n)

    # lists = []
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     lists.append([name, score])
    # lists.sort()
    # print(lists)
    # score = []
    # for i in range(len(lists)):
    #     score.append(lists[i][1])
    # print(score)
    # a = min(score)
    #
    # c = score.count(a)
    #
    # for i in range(c):
    #     score.remove(a)
    # print(min(score))
    # for i in range(len(lists)):
    #     if lists[i][1] == min(score):
    #         print(lists[i][0])

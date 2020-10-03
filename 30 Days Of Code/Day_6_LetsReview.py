T = int(input())

for _ in range(T):
    S = input()
    print(S[::2], S[1::2])

    # Alternate Approach:
    # even = ""
    # odd = ""
    # for i in range(len(S)):
    #     if i % 2 == 0:
    #         even += S[i]
    #     else:
    #         odd += S[i]
    # print(even, odd)

k = int(input())
n = input().split()
s = set()
d = set()
for i in n:
    if i not in s:
        s.add(i)
        d.add(i)
    else:
        d.discard(i)
print(d.pop())

# From Editorial:
# K = int(input())
# set_S = set()
# sum_list_S = 0
# for i in input().split():
#     I = int(i)
#     set_S.add(I)
#     sum_list_S += I
#
# print(sum(set_S))
# print(sum(set_S)*K)
# print(sum_list_S)
# print((sum(set_S)*K - sum_list_S)//(K-1))

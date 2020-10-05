n = int(input())
for i in range(n):
    A = int(input())
    set_A = set(map(int, input().split()))
    B = int(input())
    set_B = set(map(int, input().split()))
    print(set_A.issubset(set_B))
    # print(set_A <= set_B)

# From Editorial:
# for i in range(int(input())):
#     a = int(input())
#     A = set(input().split())
#     b = int(input())
#     B = set(input().split())
#     print(A <= B)

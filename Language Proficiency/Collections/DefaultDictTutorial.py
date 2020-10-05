from collections import defaultdict

n, m = map(int, input().split())

d = defaultdict(list)

for i in range(1, n+1):
    d[input().strip()].append(i)

# print(d)
# for i in d.items():
#     print(i)

for i in range(m):
    inp = input().strip()
    if inp in d.keys():
        # print(d[inp])  # without *, it will print as a list
        print(*d[inp])
    else:
        print("-1")

n, x = map(int, input().split())

lists = []
for i in range(x):
    inp = map(float, input().split())
    lists.append(list(inp))

# print(lists)

zipped = zip(*lists)
# print(list(zipped))

for num in zipped:
    print(sum(num)/x)

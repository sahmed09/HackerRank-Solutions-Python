n = int(input())
s = set(map(int, input().split()))
rep = int(input())
for i in range(rep):
    inp = [x for x in input().split(' ')]
    if inp[0] == "remove":
        s.remove(int(inp[1]))
    elif inp[0] == "discard":
        s.discard(int(inp[1]))
    elif inp[0] == "pop":
        s.pop()

print(sum(s))

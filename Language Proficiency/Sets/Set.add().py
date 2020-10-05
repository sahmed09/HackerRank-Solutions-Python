sets = set()
for _ in range(int(input())):
    name = input()
    sets.add(name)

print(len(sets))

n = int(input())
x = [input() for i in range(n)]
t = set(x)
print(len(t))

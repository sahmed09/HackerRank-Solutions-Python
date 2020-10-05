A = set(map(int, input().split()))
val = ""
for i in range(int(input())):
    inp = set(map(int, input().split()))
    if len(inp.difference(A)) == 0:
        val = "True"
    else:
        val = "False"
        break
print(val)

# From Editorial:
# The all() function returns True if all items in an iterable are true, otherwise it returns False.
# If the iterable object is empty, the all() function also returns True
A = set(input().split())
print(all(map(lambda x: (A > x), [set(input().split()) for i in range(int(input()))])))

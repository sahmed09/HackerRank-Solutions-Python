n = int(input())
s = set(map(int, input().split()))
rep = int(input())
for i in range(rep):
    cmd = (input().split())[0]
    s1 = set(map(int, input().split()))
    if cmd == "update":
        s.update(s1)
    elif cmd == "intersection_update":
        s.intersection_update(s1)
    elif cmd == "difference_update":
        s.difference_update(s1)
    elif cmd == "symmetric_difference_update":
        s.symmetric_difference_update(s1)
    # print(s)

print(sum(s))



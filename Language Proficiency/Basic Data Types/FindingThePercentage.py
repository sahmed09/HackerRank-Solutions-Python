# n = int(input())
# # n = 3
# student_marks = {}
# for i in range(n):
#     inp = [x for x in input().split(' ')]
#     student_marks[inp[0]] = [int(inp[1]), int(inp[2]), int(inp[3])]
#     # print(dicts)
# x = input()
# avg = sum(student_marks[x])/3
# print("%.2f" % avg)

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
avg = sum(student_marks[query_name])/3
print("%.2f" % avg)

from collections import namedtuple

N = int(input())
student = namedtuple('student', input().strip().split())

total = 0
for i in range(N):
    total += float(student(*input().strip().split()).MARKS)

print(total/N)

# print(sum(float(student(*input().strip().split()).MARKS) for _ in range(N))/N)

# Detailed Approach:
# N = int(input())
# fields = input().split()
#
# total = 0
# for i in range(N):
#     students = namedtuple('student', fields)
#     field1, field2, field3, field4 = input().split()
#     student = students(field1, field2, field3, field4)
#     total += int(student.MARKS)
# print('{:.2f}'.format(total/N))


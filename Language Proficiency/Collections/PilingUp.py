from collections import deque


def check(d):
    while d:
        big = d.popleft() if d[0] > d[-1] else d.pop()
        if not d:
            return "Yes"
        if d[-1] > big or d[0] > big:
            return "No"


for i in range(int(input())):
    n = int(input())
    d = deque(map(int, input().split()))
    print(check(d))


# Another Approach:
"""for _ in range(int(input())):
    _, queue = int(input()), deque(map(int, input().split()))
    # print(list(reversed(sorted(queue))))

    for cube in reversed(sorted(queue)):
        if queue[-1] == cube:
            queue.pop()
        elif queue[0] == cube:
            queue.popleft()
        else:
            print("No")
            break
    else:
        print("Yes")"""


# Another Approach(without deque):
"""for t in range(int(input())):
    n = int(input())
    lst = [int(i) for i in input().split()]
    min_list = lst.index(min(lst))
    # print(min_list)
    left = lst[:min_list]
    right = lst[min_list+1:]
    # print(sorted(left, reverse=True))
    # print(sorted(right))

    if left == sorted(left, reverse=True) and right == sorted(right):
        print("Yes")
    else:
        print("No")"""


# According to Editorial:
"""T = int(input())

for i in range(T):
    n = int(input())
    number = list(map(int, input().split()))

    d = deque(number)

    right_most = d.pop()
    left_most = d.popleft()
    current_value = left_most if left_most > right_most else right_most
    latest_pic = -1
    flag = False
    latest = 0

    while len(d) > 0:
        if right_most <= left_most <= current_value:
            current_value = left_most
            left_most = d.popleft()
            latest = left_most
        elif left_most < right_most <= current_value:
            current_value = right_most
            right_most = d.pop()
            latest = right_most
        else:
            flag = True
            break

    if flag or latest > current_value:
        print("No")
    else:
        print("Yes")"""


def palindrome(x):
    sum = 0
    temp = x
    while temp != 0:
        r = temp % 10
        sum = sum * 10 + r
        temp = temp // 10  # temp = int(temp / 10) both are same

    return sum


n = int(input())
k = list(map(int, input().split()))

lists = []
lists2 = []

for item in k:
    lists.append(item > 0)

a = all(lists)  # returns True if all the value is "True" in lists
# print(k)

if a:
    for i in k:
        res = palindrome(i)
        lists2.append(res == i)  # if res==i then i is a palindrome number and appends true
    if any(lists2):  # returns True if there is any "True" in lists2
        print(True)
    else:
        print(False)
else:
    print(False)

# Shortcut approach:
n = int(input())
k = input().split()

print(all(int(i) > 0 for i in k) and any(j == j[::-1] for j in k))

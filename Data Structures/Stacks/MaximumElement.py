# Using two lists:
items = []
maximum = []

for i in range(int(input())):
    nums = list(map(int, input().split()))
    if nums[0] == 1:
        if len(items) == 0:
            items.append(nums[1])
            maximum.append(nums[1])
        else:
            if nums[1] > maximum[-1]:
                maximum.append(nums[1])
            else:
                maximum.append(maximum[-1])
            items.append(nums[1])
    elif nums[0] == 2:
        if len(items) != 0:
            items.pop()
            maximum.pop()
    else:
        print(maximum[-1])

# Using single list:
# items = [0]
#
# for i in range(int(input())):
#     nums = list(map(int, input().split()))
#     if nums[0] == 1:
#         items.append(max(nums[1], items[-1]))
#     elif nums[0] == 2:
#         items.pop()
#     else:
#         print(items[-1])

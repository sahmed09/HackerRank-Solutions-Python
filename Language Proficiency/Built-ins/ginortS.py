inp = input()
sorted_string = sorted(inp)
# print(sorted_string)

upper = ""
lower = ""
even = ""
odd = ""

for i in sorted_string:
    if i.islower():
        lower += i
    elif i.isupper():
        upper += i
    elif int(i) % 2 != 0:
        odd += i
    elif int(i) % 2 == 0:
        even += i

# print(ord('a'))
# for i in range(len(sorted_string)):
#     # print(i)
#     if sorted_string[i] in "20468":
#         even += sorted_string[i]
#     elif sorted_string[i] in "13579":
#         odd += sorted_string[i]
#     elif 97 <= ord(sorted_string[i]) <= 122:
#         lower += sorted_string[i]
#     elif 65 <= ord(sorted_string[i]) <= 90:
#         upper += sorted_string[i]

print(lower+upper+odd+even)

# Another Approach:
upper = []
lower = []
even = []
odd = []

s = input()

for i in s:
    if i.isalpha():
        if i.isupper():
            upper.append(i)
        else:
            lower.append(i)
    else:
        if int(i) % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

upper.sort()
lower.sort()
even.sort()
odd.sort()

merge = lower+upper+odd+even

for i in merge:
    print(i, end="")
print()

import re

# sign = "[+-]?"
# decimals = "(\.[0-9]+)?"
# zeros = "(\.0+)?"
#
# latitude = f"{sign}(90{zeros}|[1-8]\d{decimals}|\d{decimals})"
# longitude = f"{sign}(180{zeros}|1[0-7]\d{decimals}|[1-9]\d{decimals}|\d{decimals})"
#
# regex = f"\({latitude}, {longitude}\)"
# pattern = re.compile(regex)
#
# for _ in range(int(input())):
#     inp = input()
#     if re.search(pattern, inp):
#         print("Valid")
#     else:
#         print("Invalid")

# Another Approach:
t = re.compile(r"""
    ^\(
    [+-]?((90(\.0+)?)|([1-8][0-9](\.[0-9]+)?)|([0-9](\.[0-9]+)?)),
    \ 
    [+-]?((180(\.0+)?)|((1[0-7][0-9]|[1-9][0-9]|[0-9])(\.[0-9]+)?))
    \)$""", re.X)

for x in range(int(input())):
    if t.match(input()):
        print("Valid")
    else:
        print("Invalid")

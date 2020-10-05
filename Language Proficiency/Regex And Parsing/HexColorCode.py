import re

# Using non-capturing group:
N = int(input())

for _ in range(N):
    S = input()
    # matches = re.findall(r"(?<!^)(#(?:[\da-fA-F]{3}){1,2})", S)
    matches = re.findall(r"(?<!^)(#(?:[\da-f]{3}){1,2})", S, re.IGNORECASE)
    if matches:
        print(*matches, sep="\n")

"""Explanations:
# matches = re.findall(r"(?<!^)(#(?:[\\da-f]{3}){1,2})", S, re.IGNORECASE)
(?<!^) means not match the start of each line, that how we erase #BED and #Cab
(?:[\\da-f]{3}){1,2} , (?: ) means we don't store the message that match in the (), which ensure us to 
store the information in (# .....{1,2}). That's how non-capturing group works.
[\\da-f]{3}{1,2} means [\\da-f]{3} or [\\da-f]{6}, re.IGNORECASE in order to get the [A-F]
"""

# Another Approach:
in_css = False
N = int(input())
for _ in range(N):
    # get the line and check for the color code
    line = input()
    if "{" in line:
        in_css = True
    elif "}" in line:
        in_css = False
    elif in_css:
        for color in re.findall('#[0-9a-fA-F]{3,6}', line):
            print(color)

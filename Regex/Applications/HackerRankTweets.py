import re

count = 0
for _ in range(int(input())):
    string = input()
    if re.search(r"hackerrank", string, re.IGNORECASE):
        count += 1

print(count)

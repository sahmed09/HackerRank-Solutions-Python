import re

for _ in range(int(input())):
    name = input()
    if re.match(r"^[A-Z]{5}[0-9]{4}[A-Z]$", name):
        print("YES")
    else:
        print("NO")

import re

for _ in range(int(input())):
    name = input()
    if re.match(r"^[_.][0-9]+[a-zA-Z]*[_]?$", name):
        print("VALID")
    else:
        print("INVALID")

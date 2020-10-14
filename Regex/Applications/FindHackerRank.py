import re

for _ in range(int(input())):
    string = input()
    if re.search(r"^hackerrank(.*hackerrank)?$", string):
        print(0)
    elif re.search(r"^hackerrank", string):
        print(1)
    elif re.search(r"hackerrank$", string):
        print(2)
    else:
        print(-1)

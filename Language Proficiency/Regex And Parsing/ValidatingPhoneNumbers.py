import re

for _ in range(int(input())):
    S = input().strip()
    # r = re.match(r"^[789][0-9]{9}$", S)
    r = re.search(r"^[789]\d{9}$", S)

    if r:
        print("YES")
    else:
        print("NO")

import re

regex_pattern = r'<(\w+)'
sets = set()
for _ in range(int(input())):
    html = input()
    res = re.findall(regex_pattern, html)
    # print(res)
    for tag in res:
        if tag not in sets:
            sets.add(tag)
# print(sorted(sets))
print(*sorted(sets), sep=";")

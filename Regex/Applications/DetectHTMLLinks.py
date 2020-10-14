import re

regex_pattern = r'<a href="(.*?)".*?>([\w ,./]*)(?=</)'

for _ in range(int(input())):
    html = input()
    res = re.findall(regex_pattern, html)
    for link, title in res:
        print(f"{link},{title.strip()}")

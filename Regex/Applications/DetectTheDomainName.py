import re

pattern = r"https?:\/\/(www\.)?(ww2\.)?([\w.-]+\.[a-z]+)"

n = int(input())
text = "\n".join(input() for _ in range(n))
url_list = []

urls = re.findall(pattern, text)
if urls:
    for url in urls:
        if url[2] not in url_list:
            url_list.append(url[2])
print(";".join(sorted(url_list)))

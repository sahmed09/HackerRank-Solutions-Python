import re
from collections import defaultdict

tags = defaultdict(set)

for _ in range(int(input())):
    html = input()
    for tag, attribute in re.findall(r"<(\w+)(.*?)?>", html):
        tags[tag].update(re.findall(r"\s(\w+)=", attribute))

for tag, attributes in sorted(tags.items()):
    print(tag + ":" + ",".join(sorted(attributes)))

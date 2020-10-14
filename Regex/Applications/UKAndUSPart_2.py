import re

n = int(input())
text = "\n".join(input() for _ in range(n))

t = int(input())
for _ in range(t):
    query = input()
    pattern = re.compile(r"\b%s\b" % query)
    print(len(re.findall(pattern, re.sub(r"ou?r", "our", text))))


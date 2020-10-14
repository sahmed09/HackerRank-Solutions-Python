import re

pattern = r"[\w\.]+@(?:\w+\.)+\w+"

n = int(input())
text = "\n".join(input() for _ in range(n))

emails = re.findall(pattern, text)
print(";".join(sorted(set(emails))))

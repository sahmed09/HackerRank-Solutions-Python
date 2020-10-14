import re
import sys

pattern = re.compile(r'href="/questions/(\d+)/.+?>(.+?)</a>.+?class="relativetime">(.+?)</span>', re.DOTALL)
fragment = sys.stdin.read()

result = re.findall(pattern, fragment)
for line in result:
    print(*line, sep=";")

import re

T = int(input())

# regex_pattern = r"^[+-]?[0-9]*\.[0-9]+$"
regex_pattern = r"^[+-]?\d*\.\d+$"
for _ in range(T):
    N = input().strip()
    # match = re.match(r"^[+\-]?[0-9]*.[0-9]+$", N)
    print(bool(re.match(regex_pattern, N)))

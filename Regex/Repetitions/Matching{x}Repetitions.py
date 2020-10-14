import re

Regex_Pattern = r'^[a-zA-Z24680]{40}[13579\s]{5}$'
print(str(bool(re.search(Regex_Pattern, input()))).lower())

import re

Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'
# Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z].*'
print(str(bool(re.search(Regex_Pattern, input()))).lower())

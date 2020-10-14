import re

Regex_Pattern = r'^(Mr|Mrs|Ms|Dr|Er)\.[a-zA-Z]+$'
# Regex_Pattern = r'^(Mr\.|Ms\.|Dr\.|Er\.|Mrs\.)[A-Za-z]+$'
print(str(bool(re.search(Regex_Pattern, input()))).lower())

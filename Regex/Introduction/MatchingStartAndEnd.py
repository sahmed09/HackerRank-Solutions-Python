import re

Regex_Pattern = r"^\d[\w]{4}\.$"
# Regex_Pattern = r"^\d\w{4}[.]$"
# Regex_Pattern = r'^\d\w\w\w\w\.$'
print(str(bool(re.search(Regex_Pattern, input()))).lower())

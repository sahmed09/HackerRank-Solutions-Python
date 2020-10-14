import re

Regex_Pattern = r"^\d\d(-?)\d\d\1\d\d\1\d\d$"
# Regex_Pattern = r"^((\d{8})|(\d{2}-){3}\d{2})$"
print(str(bool(re.search(Regex_Pattern, input()))).lower())

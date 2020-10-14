import re

Regex_Pattern = r"(\S{2}\s){2}\S{2}"
# Regex_Pattern = r"\S\S\s\S\S\s\S\S"
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# whitespace character [ \r\n\t\f ]  (\s)

import re

Regex_Pattern = r"\w{3}\W\w{10}\W\w{3}"
# Regex_Pattern = r"\w{3}\W\w+\W\w{3}"
# Regex_Pattern = r'\w\w\w\W\w\w\w\w\w\w\w\w\w\w\W\w\w\w'
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Word characters include alphanumeric characters (a-z, A-Z and 0-9) and underscores (_). (\w)

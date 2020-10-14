import re

Regex_Pattern = r'(ok){3,}'
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Parenthesis ( ) around a regular expression can group that part of regex together.
# (?: ) can be used to create a non-capturing group. It is useful if we do not need the group to capture
# its match.

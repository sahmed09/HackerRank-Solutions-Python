import re

Regex_Pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# \b assert position at a word boundary.

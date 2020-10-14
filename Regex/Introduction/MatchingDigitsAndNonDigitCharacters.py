import re

Regex_Pattern = r"([\d]{2}\D){2}[\d]{4}"
# Regex_Pattern = r'\d\d\D\d\d\D\d\d\d\d'
print(str(bool(re.search(Regex_Pattern, input()))).lower())

import re

Regex_Pattern = r'^\D[^aeiou][^bcDF]\S[^AEIOU][^\.,]$'
# Regex_Pattern = r'^[^\d][^aeiou][^bcDF][^\s][^AEIOU][^.,]$'
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# negated character class [^]

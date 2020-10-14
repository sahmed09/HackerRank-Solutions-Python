import re

Regex_Pattern = r'^[123][120][xs0][30Aa][xsu][.,]$'
print(str(bool(re.search(Regex_Pattern, input()))).lower())

# character class [ ]

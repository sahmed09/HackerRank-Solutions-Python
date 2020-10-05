import re

S = input().strip()

result = re.search(r"([0-9a-zA-Z])\1+", S)
# result = re.search(r"(\w(?!_))\1+", S)

# print(result.group(1) if result else -1)
if result:
    print(result.group(1))
else:
    print(-1)

"""
match() -------- > >> Determine if the RE matches at the beginning of the string.
search() ---------> >> Scan through a string, looking for any location where this RE matches.
findall() ---- ----->>> Find all substrings where the RE matches, and returns them as a list.
finditer()----->>> Find all substrings where the RE matches, and returns them as an iterator.
"""

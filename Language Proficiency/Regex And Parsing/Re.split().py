import re

regex_pattern = r"\D+"  # "\D+" means it matches any character that's not a digit and "+" is the quantifier.
# regex_pattern = r"[,.]"	 # Do not delete 'r'.
# regex_pattern = r"[^0-9]"	 # Do not delete 'r'.

print("\n".join(re.split(regex_pattern, input().strip())))

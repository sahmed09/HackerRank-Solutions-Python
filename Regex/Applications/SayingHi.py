import re

pattern = r"^[Hh][Ii]\s[^Dd].*"

for _ in range(int(input())):
    string = input()
    if re.match(pattern, string):
        print(string)

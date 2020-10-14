import re

pattern = re.compile(r"^[a-z]{0,3}\d{2,8}[A-Z]{3,}$")

for _ in range(int(input())):
    id_num = input()
    if re.match(pattern, id_num):
        print("VALID")
    else:
        print("INVALID")

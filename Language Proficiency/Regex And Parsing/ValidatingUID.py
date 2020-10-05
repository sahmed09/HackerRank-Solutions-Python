import re

for _ in range(int(input())):
    n = input().strip()

    if n.isalnum() and len(n) == 10:
        if bool(re.search(r"(.*[A-Z]){2,}", n)) and bool(re.search(r"(.*[0-9]){3,}", n)):
            if re.search(r".*(.).*\1+.*", n):
                print("Invalid")
            else:
                print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")

"""
Explanations:
(.*[A-Z]){2,}
.* matches any character (except for a newline).
[A-Z] matches a single character present in the range between A and Z (case sensitive).

(.*[0-9]){3,}
.* matches any character (except for a newline).
[0-9] matches a single character present in the range between 0 and 9 (case sensitive)

.*(.).*\1+.*
.* matches any character (except for a newline).
\1+ matches the same text as the most recently matched by the 1st capturing group.
"""

# Using assert(not a good choice though):
# for _ in range(int(input())):
#     u = ''.join(sorted(input()))
#     try:
#         assert re.search(r'[A-Z]{2}', u)
#         assert re.search(r'\d\d\d', u)
#         assert not re.search(r'[^a-zA-Z0-9]', u)
#         assert not re.search(r'(.)\1', u)
#         assert len(u) == 10
#     except:
#         print('Invalid')
#     else:
#         print('Valid')

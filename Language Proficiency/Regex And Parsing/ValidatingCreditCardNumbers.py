import re

for _ in range(int(input())):
    n = input().strip()

    match = re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", n) and not re.search(r"(\d)\1{3,}", n.replace("-", ""))
    if match:
        print("Valid")
    else:
        print("Invalid")

# From Editorial:
"""
Part1 :
Check if credit card number size if exactly 16, all the characters are integers and - symbol may be 
present after every group of 4 digits
All the above checks can be validated using : r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$'
Part2:
Check is credit card number has 4 or more repeating consecutive digits
This check can be validated using : r'(\d)\1{3,}'
"""
# for _ in range(int(input())):
#     n = input().strip()
#     pre_match = re.search(r"^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$", n)
#     # ? Applies to the immediately preceding character(s) and indicates to match zero or one time.
#
#     if pre_match:
#         processed_string = "".join(pre_match.group(0).split("-"))
#         final_match = re.search(r"(\d)\1{3,}", processed_string)
#         print("Invalid" if final_match else "Valid")
#     else:
#         print("Invalid")

# Another Approach(using assert not a good choice though):
# for _ in range(int(input())):
#     n = input().strip()
#     try:
#         assert re.match(r"^(\d{4}-){3}\d{4}$", n) or re.match(r"^\d{16}$", n)
#         n = re.sub("-", "", n)
#         assert re.match(r"[456]", n)
#         assert not re.search(r"(\d)\1{3,}", n)
#         print("Valid")
#     except:
#         print("Invalid")

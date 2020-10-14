import re

for _ in range(int(input())):
    ip = input().strip()
    if re.match(r"^(([0-9]|[01]?[0-9][0-9]|2[0-4]\d|25[0-5])\.){3}([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])$", ip):
        print("IPv4")
    elif re.match(r"^(([0-9a-fA-F]{1,4}):){7}([0-9a-f]{1,4})$", ip):
        print("IPv6")
    else:
        print("Neither")

"""
IPv4:
^([0-9]|[01]?[0-9][0-9]|2[0-4][0-9]|25[0-5])(\\.([0-9]|[01]?[0-9][0-9]|2[0-4][0-9]|25[0-5])){3}$
This can be split into two parts:
1.The base: ([0-9]|[01]?[0-9][0-9]|2[0-4][0-9]|25[0-5])
The ^ checks that the beginning of the string matches any of the following:
[0-9]: A single digit in the inclusive range from 0 to 9.
[01]?[0-9][0-9]: A two-digit number in the inclusive range from 00 to 99 that may be preceded by a 0 or 1 
    (i.e., it basically matches 000 to 199).
2[0-4][0-9]: A three-digit number in the inclusive range between 200 and 249.
25[0-5]: A three-digit number in the inclusive range between 250 and 255.
2.The repeated part: (\\.([0-9]|[01]?[0-9][0-9]|2[0-4][0-9]|25[0-5])){3}$
This matches a period (.) immediately followed by the base statement above exactly three times ({3}) before checking 
that there is nothing else in the string ($).

IPv6:
^([0-9a-fA-F]{1,4})(:([0-9a-fA-F]{1,4})){7}$
This can be split into two parts:
1.The base: ^[0-9A-Fa-f]{1,4}
The ^ checks that the beginning of the string matches [0-9A-Fa-f]{1,4}, meaning it's a digit in the inclusive range 
    from 0 to 9 or an English alphabetic letter (upper or lowercase) that occurs anywhere between 1 and 4 times ({1,4}).
2.The repeated part: (:([0-9a-fA-F]{1,4})){7}
This matches a colon (:) immediately followed by the base statement above exactly seven times ({7}) before checking 
    that there is nothing else in the string ($).
"""

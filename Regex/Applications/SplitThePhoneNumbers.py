import re

pattern = re.compile(r"(\d{1,3})[\s-](\d{1,3})[\s-](\d{4,10})")
for _ in range(int(input())):
    phone = input()
    match = re.search(pattern, phone)
    print("CountryCode=" + match.group(1) + ",LocalAreaCode=" + match.group(2) + ",Number=" + match.group(3))

# for test in range(int(input())):
#     match = re.match(r'(\d{1,3})[ \-](\d{1,3})[ \-](\d{4,10})', input()).groups()
#     if match:
#         print('CountryCode=%s,LocalAreaCode=%s,Number=%s' % match)

# Without Regex:
# n = int(input())
# for _ in range(n):
#     phone = input()
#     if ' ' in phone:
#         country, area, number = phone.split()
#     elif '-' in phone:
#         country, area, number = phone.split('-')
#     print("CountryCode=" + country + ",LocalAreaCode=" + area + ",Number=" + number)


# Using Decorator:
# def Wrapper(func):
#     def Decorate(Num):
#         Num = func(Num)
#         return "CountryCode=%s,LocalAreaCode=%s,Number=%s" % Num
#     return Decorate
#
# @Wrapper
# def PhoneNumber(Num):
#     return re.match(r'(\d{1,3})[ \-](\d{1,3})[ \-](\d{4,10})', Num).groups();
#
#
# for _ in range(int(input())):
#     print(PhoneNumber(input().strip()))

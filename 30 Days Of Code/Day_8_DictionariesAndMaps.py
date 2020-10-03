import sys

phone_book = {}
for _ in range(int(input())):
    name, phone = input().split()
    phone_book[name] = phone
# print(dic)

# Process Queries: (ctrl+d) to stop
lines = sys.stdin.readlines()
for i in lines:
    name = i.strip()
    if name in phone_book:
        print(name + '=' + str(phone_book[name]))
    else:
        print('Not found')

# (ctrl+d) to stop
# while True:
#     try:
#         name = input()
#         if name in phone_book.keys():
#             print(name + "=" + phone_book[name])
#         else:
#             print("Not found")
#     except:
#         break

from collections import OrderedDict

N = int(input())
ordered_dictionary = OrderedDict()

for i in range(N):
    item, space, price = input().rpartition(" ")
    if item in ordered_dictionary.keys():
        ordered_dictionary[item] += int(price)
    else:
        ordered_dictionary[item] = int(price)
# print(ordered_dictionary)

for item, price in ordered_dictionary.items():
    print(item, price)

# for i in ordered_dictionary.keys():
#     print(i, ordered_dictionary[i])

# s = "A Quick Brown Fox".rpartition(" ")
# print(s)

# d = OrderedDict()
# for _ in range(int(input())):
#     item, space, quantity = input().rpartition(' ')
#     d[item] = d.get(item, 0) + int(quantity)
# for item, quantity in d.items():
#     print(item, quantity)

import re

n = int(input())
text = "\n".join(input() for _ in range(n))

t = int(input())
for _ in range(t):
    query = input()
    pattern = re.compile(r"%s[sz]e" % query[:-2])
    print(len(re.findall(pattern, text)))

# string = ''
# for n in range(int(input())):
#     string += input()
#
# for n in range(int(input())):
#     query = input()
#     print(len(re.findall(query[:len(query) - 2] + '[sz]e', string)))

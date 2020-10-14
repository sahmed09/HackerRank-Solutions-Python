import re

n = int(input())
text = "\n".join(input() for _ in range(n))
# print(text)
test = int(input())
for _ in range(test):
    query = input().strip()
    # print(len(re.findall(r"\B" + query + r"\B", text)))
    # print(len(re.findall(r'\w%s\w' % query, text)))
    print(len(re.findall(r'(?<=\w)%s(?=\w)' % query, text)))

# \B -> Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word.
# \b -> Returns a match where the specified characters are at the beginning or at the end of a word.

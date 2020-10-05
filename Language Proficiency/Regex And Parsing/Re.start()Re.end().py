import re

S = input().strip()
K = input().strip()

pattern = re.compile(K)
# print(pattern)
r = pattern.search(S)
# print(r)

if not r:
    print("(-1, -1)")
while r:
    print("({0}, {1})".format(r.start(), r.end()-1))
    r = pattern.search(S, r.start()+1)
    # print(r)

# Another Approach:
S = input()
k = input()
anymatch = 'No'
for m in re.finditer(r'(?=('+k+'))', S):
    anymatch = 'Yes'
    print((m.start(1), m.end(1)-1))
if anymatch == 'No':
    print((-1, -1))

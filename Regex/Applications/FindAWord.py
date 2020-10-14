import re

n = int(input())
text = "\n".join(input() for _ in range(n))
# print(text)
test = int(input())
for _ in range(test):
    query = input().strip()
    # res = re.finditer(rf"\b{query}\b", text)
    # for r in res:
    #     print(r)
    print(len(re.findall(rf"\b{query}\b", text)))
    # print(len(re.findall(rf"((?<=[\W])|^){query}((?=[\W])|$)", text)))

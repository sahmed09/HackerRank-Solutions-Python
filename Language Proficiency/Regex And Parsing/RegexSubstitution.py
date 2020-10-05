import re

N = int(input())

for _ in range(N):
    S = input()
    print(re.sub(r"(?<= )\|\|(?= )", "or", re.sub(r"(?<= )&&(?= )", "and", S)))
    # (?<= ) which is a positive lookbehind that makes sure that the pattern is preceded by a space.
    # (?= ) which is a positive lookahead that makes sure that the pattern is followed by a space.

# Another Approach:
for line in range(int(input())):
    string = re.sub(r"(?<= )&&(?= )", "and", input())
    string = re.sub(r"(?<= )\|\|(?= )", "or", string)
    print(string)

# Another Approach(Using lambda):
N = int(input())
for i in range(N):
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', input()))

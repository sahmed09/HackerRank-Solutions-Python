import re
import sys

pattern = r"//.*|/\*[\S\s]*?\*/"

string = "\n".join([i.strip() for i in sys.stdin])
comment = re.findall(pattern, string)
print(*comment, sep="\n")

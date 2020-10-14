import re
import sys

C = re.compile(r".*(#\s*include\s*(<\s*[\w/]+(\.\w+)?\s*>|\"[\w/]+(\.\w+)?\"\s*)).*", re.DOTALL)

JAVA = re.compile(r".*(^(public\s+|private\s+|protected\s+)*.*\w+\(.*?\)\s*{|import\s+[\w.*]+;).*", re.DOTALL)

PYTHON = re.compile(r".*(^print\s\".*\"$|^#\s.*$|def\s.*$|^if\s[^()]+:).*", re.DOTALL)

# C = re.compile(r"(?s).*(#\s*include\s*(<\s*[\w/]+(\.\w+)?\s*>|\"[\w/]+(\.\w+)?\"\s*))(?s).*")
# JAVA = re.compile(r"(?s).*(^(public\s+|private\s+|protected\s+)*.*\w+\(.*?\)\s*{|import\s+[\w.*]+;)(?s).*")
# PYTHON = re.compile(r"(?s).*(^print\s\".*\"$|^#\s.*$|def\s.*$|^if\s[^()]+:)(?s).*")

code = sys.stdin.read()

if re.search(C, code):
    print("C")
elif re.search(JAVA, code):
    print("Java")
elif re.search(PYTHON, code):
    print("Python")

import re

pattern = re.compile(r"^(C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|"
                     r"JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$")

for _ in range(int(input())):
    name, language = input().split()
    if re.match(pattern, language):
        print("VALID")
    else:
        print("INVALID")

import re

S = input().strip()

vowels = "aeiou"
consonants = "qwrtypsdfghjklzxcvbnm"
regex_pattern = "(?<=[" + consonants + "])([" + vowels + "]{2,})[" + consonants + "]"
# regex_pattern = r'(?<=[' + consonants + '])([' + vowels + ']{2,})(?=[' + consonants + '])'

match = re.findall(regex_pattern, S, re.IGNORECASE)
# match = re.findall(regex_pattern, S, flags=re.IGNORECASE)

if match:
    print(*match, sep="\n")
else:
    print("-1")

"""
positive lookahead means that you want your pattern to be followed by a specific character/expression.
positive lookahead: (?=\\d) to the right of your pattern you insert the opening parenthesis followed by a 
question mark and an equals sign: [pattern](?=  -> [pattern](?=[expression])
negative lookahead means that you want your pattern to be followed by anything but certainly not by a 
specific character/expression.
negative lookahead: (?!\\d) to the right of your pattern you insert the opening parenthesis followed by 
a question mark and an exclamation point: [pattern](?!  -> [pattern](?![expression])

(?=...)
Matches if ... matches next, but doesn’t consume any of the string. This is called a lookahead assertion.
For example, Isaac (?=Asimov) will match 'Isaac ' only if it’s followed by 'Asimov'.

(?<=...)
Matches if the current position in the string is preceded by a match for ... that ends at the current 
position. This is called a positive lookbehind assertion. (?<=abc)def will find a match in abcdef, 
since the lookbehind will back up 3 characters and check if the contained pattern matches.
"""

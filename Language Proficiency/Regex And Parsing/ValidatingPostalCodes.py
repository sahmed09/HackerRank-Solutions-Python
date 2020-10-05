import re

regex_integer_in_range = r"^[1-9][\d]{5}$"  # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=.\1)"  # Do not delete 'r'.
# regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"  # Do not delete 'r'.
# regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"  # Do not delete 'r'.

P = input()

print(bool(re.match(regex_integer_in_range, P)) and
      len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

"""
r"(\d)(?=.\1)"
The (\d) captures any digit. The (?=) is a positive look-ahead. Positive look-aheads see if there is a 
match without actually matching them (so that they can be used to find additional matches instead of 
being registered as already being "checked"). The period (?=.) matches anything that follows the first 
digit. The \1 is a reference back to the original capturing group (\d). So basically "match a digit, 
then check to see if there is anything next (.) followed by the same original digit (\1)

r"(\d)(?=\d\1)"
the first parentheses-delimited expression inside of the regex. It will return the number of alternate 
matching pattern which should be at max 1. SO the condition is of <2. re.findall function will take a 
pattern and a string. So we matches the digit \d. (?=...) Matches if ... matches next, but doesn’t 
consume any of the string. This is called a lookahead assertion. For example, Isaac (?=Asimov) will 
match 'Isaac ' only if it’s followed by 'Asimov'.

(?=(\d)\d\1) 
using this regex findall how many alternating repetitive digits are there.
"""

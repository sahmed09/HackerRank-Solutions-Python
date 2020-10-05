import re

thousand = "M{0,3}"
hundred = "(C[MD]|D?C{0,3})"
ten = "(X[CL]|L?X{0,3})"
single = "(I[VX]|V?I{0,3})"

regex_pattern = r"^" + thousand + hundred + ten + single + "$"
print(str(bool(re.match(regex_pattern, input()))))

# Single Line Approach:
pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
print(bool(re.search(pattern, input())))

# Without Regular Expression:
"""from roman import fromRoman

try:
    print(0 < fromRoman(input()) < 4000)
except:
    print(False)"""

"""
https://stackoverflow.com/questions/267399/how-do-you-match-only-valid-roman-numerals-with-a-regular-expression
Individual decimal places
Thousands	Hundreds	Tens	Units
1	M	       C	     X	      I
2	MM	       CC	     XX	      II
3	MMM	       CCC	     XXX	  III
4		       CD	     XL	      IV
5		       D	     L	      V
6		       DC	     LX	      VI
7		       DCC	     LXX	  VII
8		       DCCC	     LXXX	  VIII
9		       CM	     XC	      IX

M{0,4} specifies the thousands section and basically restrains it to between 0 and 4000
   0: <empty>  matched by M{0}
1000: M        matched by M{1}
2000: MM       matched by M{2}
3000: MMM      matched by M{3}

(CM|CD|D?C{0,3}), this is for the hundreds section
  0: <empty>  matched by D?C{0} (with D not there)
100: C        matched by D?C{1} (with D not there)
200: CC       matched by D?C{2} (with D not there)
300: CCC      matched by D?C{3} (with D not there)
400: CD       matched by CD
500: D        matched by D?C{0} (with D there)
600: DC       matched by D?C{1} (with D there)
700: DCC      matched by D?C{2} (with D there)
800: DCCC     matched by D?C{3} (with D there)
900: CM       matched by CM

(XC|XL|L?X{0,3}) for the tens place
 0: <empty>  matched by L?X{0} (with L not there)
10: X        matched by L?X{1} (with L not there)
20: XX       matched by L?X{2} (with L not there)
30: XXX      matched by L?X{3} (with L not there)
40: XL       matched by XL
50: L        matched by L?X{0} (with L there)
60: LX       matched by L?X{1} (with L there)
70: LXX      matched by L?X{2} (with L there)
80: LXXX     matched by L?X{3} (with L there)
90: XC       matched by XC

(IX|IV|V?I{0,3}) is the units section, handling 0 through 9
0: <empty>  matched by V?I{0} (with V not there)
1: I        matched by V?I{1} (with V not there)
2: II       matched by V?I{2} (with V not there)
3: III      matched by V?I{3} (with V not there)
4: IV       matched by IV
5: V        matched by V?I{0} (with V there)
6: VI       matched by V?I{1} (with V there)
7: VII      matched by V?I{2} (with V there)
8: VIII     matched by V?I{3} (with V there)
9: IX       matched by IX
(?<=^)M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})(?=$)
"""

import math
# import cmath

AB = float(input())
BC = float(input())

print(round(math.degrees(math.atan(AB/BC))), chr(176), sep="")
# print(round(math.degrees(math.atan2(AB, BC))), chr(176), sep="")
# print(str(round(math.degrees(math.atan2(AB, BC)))) + u"\N{DEGREE SIGN}")
# print(str(int(round(math.degrees(cmath.phase(complex(BC, AB))))))+'°')

# print(chr(176))  # represents degree

from math import exp, factorial

lambdaa = float(input())
k = int(input())

probability = ((lambdaa ** k) * exp(-lambdaa)) / factorial(k)
print(round(probability, 3))

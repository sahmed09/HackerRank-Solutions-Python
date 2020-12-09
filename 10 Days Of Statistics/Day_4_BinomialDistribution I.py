from math import factorial


def binomial_dist(x, n, p):
    result = (factorial(n) / factorial(x) / factorial(n - x)) * (p ** x) * ((1 - p) ** (n - x))
    return result


binomial_result = 0
p = 1.09 / (1 + 1.09)  # probability of being a boy
n = 6  # total number of trials

for i in range(3, 7):
    binomial_result += binomial_dist(i, n, p)

print(round(binomial_result, 3))

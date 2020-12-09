from math import factorial


def binomial_dist(x, n, p):
    result = (factorial(n) / factorial(x) / factorial(n - x)) * (p ** x) * ((1 - p) ** (n - x))
    return result


p, n = list(map(int, input().split(" ")))  # p = probability of success of 1 trial, n = total number of trials

no_more_two_reject = 0
for i in range(3):
    no_more_two_reject += binomial_dist(i, n, p / 100)

at_least_two_reject = 0
for i in range(2, n+1):
    at_least_two_reject += binomial_dist(i, n, p / 100)

print(round(no_more_two_reject, 3))
print(round(at_least_two_reject, 3))

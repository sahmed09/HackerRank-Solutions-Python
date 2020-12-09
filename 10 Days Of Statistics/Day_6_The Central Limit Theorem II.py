from math import erf, sqrt  # erf = error function

x = int(input())  # 250
n = int(input())  # 4100
mean = float(input())  # 2.4
std_dev = float(input())  # 2.0

mean_total = n * mean
std_dev_total = sqrt(n) * std_dev


def normal_dist(x, mean, std_dev):
    return 0.5 * (1 + erf((x - mean) / (std_dev * sqrt(2))))


print(round(normal_dist(x, mean_total, std_dev_total), 4))  # 0.6915

from math import sqrt

samples = int(input())  # 100
mean = int(input())  # 500
std = int(input())  # 80
interval = float(input())  # 0.95
z = float(input())  # 1.96

print(round(mean - (std / sqrt(samples)) * z, 2))  # 484.32
print(round(mean + (std / sqrt(samples)) * z, 2))  # 515.68

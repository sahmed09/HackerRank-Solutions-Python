import math

n = int(input())
data = list(map(int, input().split()))

mean = sum(data) / n
# print(mean)

sq_mean = 0
for i in data:
    sq_mean += (i - mean) ** 2
# print(sq_mean)

variance = (sq_mean / n)
# print(variance)

std_dev = round(math.sqrt(variance), 1)
print(std_dev)

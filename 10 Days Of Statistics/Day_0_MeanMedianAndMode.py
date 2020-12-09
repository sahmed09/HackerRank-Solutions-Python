from collections import Counter

n = int(input())
data = sorted(list(int(i) for i in input().split()))

# Mean
mean = sum(data) / n
print(mean)

# Median
if n % 2 == 0:
    median = (data[int(n / 2) - 1] + data[int(n / 2)]) / 2
else:
    median = data[int((n + 1) / 2)]
print(median)

# Mode:
counts = Counter(data)
freq = 0
mode = 0
for val, count in counts.items():
    if count > freq:
        mode = val
        freq = count

    elif count == freq and val < mode:
        mode = val
print(mode)

# import numpy as np
# from scipy import stats
#
# size = int(input())
# numbers = list(map(int, input().split()))
# print(np.mean(numbers))
# print(np.median(numbers))
# print(int(stats.mode(numbers)[0]))

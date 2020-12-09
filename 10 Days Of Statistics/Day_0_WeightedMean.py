n = int(input())
data = list(map(int, input().split()))
weight = list(map(int, input().split()))

total = 0
total_weight = 0
for i in range(n):
    total += data[i] * weight[i]
    total_weight += weight[i]

mean = round(total / total_weight, 1)
print(mean)

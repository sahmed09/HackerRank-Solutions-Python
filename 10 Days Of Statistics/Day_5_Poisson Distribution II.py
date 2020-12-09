mean_a, mean_b = list(map(float, input().split(" ")))

cost_a = 160 + 40 * (mean_a + mean_a ** 2)
cost_b = 128 + 40 * (mean_b + mean_b ** 2)

print(round(cost_a, 3))
print(round(cost_b, 3))

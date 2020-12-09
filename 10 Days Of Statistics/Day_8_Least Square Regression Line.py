# x = [95,85,80,70,60]
# y = [85,95,70,65,70]

""" ***Using Maths Formula*** """
x, y = [], []
for _ in range(5):
    xy = list(map(int, input().split()))
    x.append(xy[0])
    y.append(xy[1])

n = len(x)
x_sum = sum(x)
x_sum_sqr = x_sum ** 2
x_sqr_sum = sum([x_i ** 2 for x_i in x])
y_sum = sum(y)
sum_prod_xy = 0
for x_i, y_i in zip(x, y):
    sum_prod_xy += (x_i * y_i)
b = ((n * sum_prod_xy) - (x_sum * y_sum)) / ((n * x_sqr_sum) - x_sum_sqr)  # Calculating the Slope

x_mean = x_sum / n
y_mean = y_sum / n
a = y_mean - (b * x_mean)  # Calculating the Intercept

# to make prediction
x_test = 80
y_test = a + b * x_test
print(round(y_test, 3))  # 78.288

""" ***Using Pearson Correlation Coefficient*** """
# from statistics import mean, pstdev  # pstdev -> standard deviation
#
#
# def pearson(x, y):
#     n = len(x)
#     mean_x, std_dev_x, mean_y, std_dev_y = mean(x), pstdev(x), mean(y), pstdev(y)
#     correlation_coefficient = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)) / (n * std_dev_x * std_dev_y)
#     return correlation_coefficient
#
#
# def linear_regression(x, y):
#     b = pearson(x, y) * pstdev(y) / pstdev(x)  # Calculating the Slope
#     a = mean(y) - b * mean(x)  # Calculating the Intercept
#     return a, b
#
#
# x, y = [], []
# for _ in range(5):
#     xy = list(map(int, input().split()))
#     x.append(xy[0])
#     y.append(xy[1])
# a, b = linear_regression(x, y)
#
# # to make prediction
# x_test = 80
# y_test = a + b * x_test
# print(round(y_test, 3))  # 78.288

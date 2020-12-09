import math


def means(data):
    return sum(data) / len(data)


def std_dev(data):
    mean = sum(data) / len(data)

    sq_mean = 0
    for i in data:
        sq_mean += (i - mean) ** 2

    variance = (sq_mean / len(data))
    standard_deviation = math.sqrt(variance)
    return standard_deviation


if __name__ == '__main__':
    n = int(input())
    data_x = list(map(float, input().split()))
    data_y = list(map(float, input().split()))

    mean_x = means(data_x)
    std_dev_x = std_dev(data_x)

    mean_y = means(data_y)
    std_dev_y = std_dev(data_y)

    covariance = 0
    for i in range(n):
        covariance += ((data_x[i] - mean_x) * (data_y[i] - mean_y))

    correlation_coefficient = covariance / (n * std_dev_x * std_dev_y)

    print(round(correlation_coefficient, 3))

from math import erf, sqrt  # erf = error function

mean, std_dev = 20, 2
time = 19.5
lower_time, upper_time = 20, 22


def normal_dist(mean, std_dev, x):
    return 0.5 * (1 + erf((x - mean) / (std_dev * sqrt(2))))


print(round(normal_dist(mean, std_dev, time), 3))  # Less than 19.5 hours
# Between 20 and 22 hours
print(round(normal_dist(mean, std_dev, upper_time) - normal_dist(mean, std_dev, lower_time), 3))

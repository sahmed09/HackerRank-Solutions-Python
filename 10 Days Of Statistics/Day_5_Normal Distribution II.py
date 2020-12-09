from math import erf, sqrt  # erf = error function

mean, std_dev = 70, 10
score_higher = 80
threshold = 60


def normal_dist(mean, std_dev, x):
    return 0.5 * (1 + erf((x - mean) / (std_dev * sqrt(2))))


print(round((1 - normal_dist(mean, std_dev, score_higher)) * 100, 2))  # Scored higher than 80
print(round((1 - normal_dist(mean, std_dev, threshold)) * 100, 2))  # Passed the test, grade >= 60
print(round(normal_dist(mean, std_dev, threshold) * 100, 2))  # Failed the test, grade < 60

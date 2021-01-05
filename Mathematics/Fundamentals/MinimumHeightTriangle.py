import math


def lowestTriangle(base, area):
    if (2*area) % base == 0:
        return (2*area) // base
    else:
        return (2 * area) // base + 1

    # return (2*area - 1) // base + 1  # Another Approach
    # return math.ceil((2*area)/base)  # Another Approach


base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)

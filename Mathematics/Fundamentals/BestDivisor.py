# def getDigitSum(k):
#     total = 0
#     while k > 0:
#         total += k % 10
#         k //= 10
#     return total


def getBestDivisior(n):
    max_sum = 1
    best_number = 1

    for i in range(2, n+1):
        if n % i == 0:
            digit_sum = sum(map(int, str(i)))
            # digit_sum = getDigitSum(i)  # can be used instead of previous line

            # Only need to track one number because if two numbers have same digitSum, smaller (previously
            # stored value) is better.

            if digit_sum > max_sum:
                max_sum = digit_sum
                best_number = i
    return best_number


if __name__ == '__main__':
    n = int(input())
    print(getBestDivisior(n))

# Shortcut Solution(One Line):
# print(max((d for d in range(1, n + 1) if n % d == 0), key=lambda x: sum(map(int, str(x)))))

# Another Solution:
"""def abc(n):
    return sum([int(i) for i in list(str(n))])


if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(1, n + 1):
        if n % i == 0:
            a.append(i)
    print(max(a, key=abc))
"""

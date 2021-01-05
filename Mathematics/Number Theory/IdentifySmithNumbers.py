from math import sqrt


def sum_of_digits(num):
    return num if num < 10 else num % 10 + sum_of_digits(num // 10)


def solve(num):
    temp = num
    prime_factors = []
    for i in range(2, int(sqrt(temp))+1):
        while num % i == 0:
            prime_factors.append(i)
            num //= i

    if num > 1:
        prime_factors.append(num)

    sum_of_prime_factors = 0
    for number in prime_factors:
        sum_of_prime_factors += sum_of_digits(number)

    if sum_of_prime_factors == sum_of_digits(temp):
        return 1
    else:
        return 0


if __name__ == '__main__':
    n = int(input())

    # result = is_smith(n)
    result = solve(n)
    print(result)


# def sum_of_digits(num):
#     return num if num < 10 else num % 10 + sum_of_digits(num // 10)
#
#
# def is_smith(num):
#     digits_sum = sum_of_digits(num)
#     sum_of_factors, p = 0, 2
#
#     while p*p <= num:
#         if num % p:
#             p += 1
#         else:
#             num = num // p
#             sum_of_factors += sum_of_digits(p)
#
#     ans = int(digits_sum == sum_of_factors + sum_of_digits(num))
#     if num > 1:
#         return ans
#     else:
#         return 0

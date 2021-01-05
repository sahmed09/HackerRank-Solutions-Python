import os
import math


def divisors(n):
    count = 0
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0 and i % 2 == 0:
            count += 1
        if n % (n // i) == 0 and (n // i) % 2 == 0 and n // i != i:
            count += 1
    if n % 2 == 0:
        count += 1
    return count

# def divisors(n):
#     count = 0
#     for i in range(1, int(math.sqrt(n))+1):
#         if n % i == 0 and i % 2 == 0:
#             count += 1  # i is even
#         if n % (n//i) == 0 and (n//i) % 2 == 0:
#             count += 1  # n//i is even and n's factor
#         if i == n // i and i % 2 == 0 and n % i == 0:
#             count -= 1  # if i is sqrt reduce by 1
#     return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = divisors(n)
        print(result)

        # fptr.write(str(result) + '\n')
    # fptr.close()

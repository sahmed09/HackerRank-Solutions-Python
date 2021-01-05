import os


def summingSeries(n):
    mod = pow(10, 9) + 7
    return pow(n, 2, mod)
    # return pow(n, 2) % mod
    # return pow(n, 2, 10**9+7)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = summingSeries(n)
        print(result)

        # fptr.write(str(result) + '\n')
    # fptr.close()

# Time Complexity : O(1)
# Answer = n**2 mod (10**9 + 7)

"""
Closed Form:
An equation is said to be a closed-form solution if it solves a given problem in terms of functions and 
mathematical operations from a given generally-accepted set.

For example, the sum of the first N numbers is given by the closed form = (N(N+1))/2
"""
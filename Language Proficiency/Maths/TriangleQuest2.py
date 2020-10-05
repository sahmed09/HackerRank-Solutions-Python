for i in range(1, int(input())+1):
    print((pow(10, i)//9)**2)

"""
(10/9)**2     = 1**2     = 1
(100/9)**2    = 11**2    = 121
(1000/9)**2   = 111**2   = 12321
(10000/9)**2  = 1111**2  = 1234321
(100000/9)**2 = 11111**2 = 123454321
"""

# for i in range(1, int(input())+1):
#     print((10**i//9)**2)

# from functools import reduce
# for i in range(1, int(input())+1):
#     print(reduce(lambda x, y: x + (10 ** (y - 1)), range(1, i + 1))**2)

# for i in range(1, int(input())+1):
#     print([1, 121, 12321, 1234321, 123454321, 12345654321, 1234567654321, 123456787654321, 12345678987654321][i-1])

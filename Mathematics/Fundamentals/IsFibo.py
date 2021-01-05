def solve(n):
    # Using Binet's Formula: for x to be a Fibonacci number, 5x^2+4 or 5x^2-4 must be a perfect square.
    root1 = (5 * n ** 2 + 4) ** 0.5
    root2 = (5 * n ** 2 - 4) ** 0.5

    is_square = root1 % 1 == 0 or root2 % 1 == 0
    if is_square:
        return "IsFibo"
    else:
        return "IsNotFibo"


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)
        print(result)

# def solve(n):
#     fibo = [0]
#     a = 0
#     b = 1
#     while True:
#         c = a + b
#         if c < 10 ** 10:
#             a = b
#             b = c
#             fibo.append(c)
#         else:
#             break
#
#     # ans = ""
#     # for i in range(len(fibo)):
#     #     if fibo[i] == n:
#     #         ans = "IsFibo"
#     #         break
#     #     else:
#     #         ans = "IsNotFibo"
#     # return ans
#
#     if n in fibo:
#         return "IsFibo"
#     else:
#         return "IsNotFibo"

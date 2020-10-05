x, k = map(int, input().split())
poly = input()

print(eval(poly) == k)

"""x**3 + x**2 + x + 1 => while evaluating, x is replaced by input x.
input variable name should be similar to polynomial variable."""

# if eval(poly) == k:
#     print(True)
# else:
#     print(False)



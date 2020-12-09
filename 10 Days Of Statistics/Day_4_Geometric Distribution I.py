p = 1 / 3  # probability that the product is defective
n = 5
q = 1 - p  # probability of the product not being defective

geometrical_result = (q ** (n - 1)) * p

print(round(geometrical_result, 3))

p = 1 / 3  # probability that product is defective
n = 5  # Total inspections
q = 1 - p  # probability of the product not being defective

# q**n A defect is not found during the first n=5 inspections.
geometrical_result = 1 - (q ** n)  # defect is found during the first n=5 inspections

print(round(geometrical_result, 3))

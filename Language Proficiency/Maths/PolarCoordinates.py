import cmath

c = complex(input().strip())
# print(c)

polar = cmath.polar(c)
# print(polar)

print(polar[0])
print(polar[1])

# abs(complex(x, y))  # modulus "r"
# cmath.phase(complex(x, y))  # phase angle "phi"

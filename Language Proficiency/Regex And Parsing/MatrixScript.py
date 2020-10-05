import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
# print(matrix)

encoded_string = ""
for i in range(m):
    for j in range(n):
        encoded_string += matrix[j][i]
print(encoded_string)

# pattern = r"(?<=[a-zA-Z0-9])([^a-zA-Z0-9]+)(?=[a-zA-Z0-9])"
"""Using (?<=[A-Za-z0-9])([^A-Za-z0-9]+)(?=[A-Za-z0-9]) this regex we can substitute all non 
alphanumeric characters between two alphanumeric characters."""
pattern = r"(?<=\w)([^\w]+)(?=\w)"
# "\w" Returns a match where the string contains any word characters.
# "\W" Returns a match where the string DOES NOT contain any word characters.
# (?<=\w) which is a positive lookbehind that makes sure that the pattern is preceded by a alphanumeric character.
# (?=\w) which is a positive lookahead that makes sure that the pattern is followed by a alphanumeric character.

print(re.sub(pattern, " ", encoded_string))

import numpy as np

# Find the solution [x, y] for the matrix equation xA + yI = -A^2, where x and y are scalars
A = np.array([[1, 1, 0],
              [0, 1, 0],
              [0, 0, 1]])

# The identity matrix
I = np.identity(3)

# Convert system to the form Bz = c:
# B is a two column matrix whose columns are flattened A and I.
B = np.array([A.flatten(), I.flatten()]).transpose()  # 9x2 matrix

# c is a column vector that is flattened A^2.
c = -1 * np.linalg.matrix_power(A, 2).flatten().transpose()  # 9x1 matrix
print(c)

# Solve Bz = -c
z = np.linalg.lstsq(B, c, rcond=-1)[0]
z = np.array(z)
print(z)

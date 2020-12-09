import numpy as np

m, n = map(int, input().split())
X, Y = [], []
for _ in range(n):
    data = input().strip().split(" ")
    X.append(data[:m])
    Y.append(data[m:])

q = int(input())
X_new = []
for _ in range(q):
    X_new.append(input().strip().split(" "))

X = np.array(X, float)
Y = np.array(Y, float)
X_new = np.array(X_new, float)

# center the data to avoid the constant
X_R = X - np.mean(X, axis=0)
Y_R = Y - np.mean(Y)

# calculate beta:
beta = np.dot(np.linalg.inv(np.dot(X_R.T, X_R)), np.dot(X_R.T, Y_R))

# predict:
X_new_R = X_new - np.mean(X, axis=0)
Y_new_R = np.dot(X_new_R, beta)
Y_new = Y_new_R + np.mean(Y)

# print:
for i in Y_new:
    print(round(float(i), 2))

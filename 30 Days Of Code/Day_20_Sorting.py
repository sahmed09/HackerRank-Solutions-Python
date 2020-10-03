n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
numSwaps = 0

for i in range(n):
    currentSwaps = 0

    for j in range(0, n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            currentSwaps += 1
            numSwaps += 1

    if currentSwaps == 0:
        break

print("Array is sorted in " + str(numSwaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[n - 1]))

# Alternate:
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

numberOfSwaps = 0
for i in range(n):
    for j in range(n-1):
        if a[j] > a[j+1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            numberOfSwaps += 1

    if numberOfSwaps == 0:
        break

print(f"Array is sorted in {numberOfSwaps} swaps.")
print("First Element:", a[0])
print("Last Element:", a[n-1])

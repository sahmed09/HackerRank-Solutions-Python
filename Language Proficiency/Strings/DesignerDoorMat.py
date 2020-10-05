row, column = map(int, input().split(' '))

for i in range(1, row, 2):
    print((".|."*i).center(column, "-"))

print("WELCOME".center(column, "-"))

for i in range(row-2, -1, -2):
    print((".|."*i).center(column, "-"))

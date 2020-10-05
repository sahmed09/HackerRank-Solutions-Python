t = int(input())

for _ in range(t):
    a, b = input().split()

    try:
        print(int(a) // int(b))
    except Exception as e:
        print("Error Code:", e)

# Another Approach:
for i in range(int(input())):
    try:
        a, b = list(map(int, input().split()))
        print(a//b)
    except ZeroDivisionError as e:
        print('Error Code:', e)
    except ValueError as e:
        print('Error Code:', e)

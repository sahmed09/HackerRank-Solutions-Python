def quartile(data):
    size = len(data)
    if size % 2 == 0:
        return (data[size // 2 - 1] + data[size // 2]) // 2
    else:
        return data[size // 2]


n = int(input())
data = list(map(int, input().split()))
data.sort()
# print(data)

if n % 2 == 0:
    lower_half = data[0:n // 2]
    upper_half = data[n // 2:n]
    q1 = quartile(lower_half)
    q2 = quartile(data)
    q3 = quartile(upper_half)
else:
    lower_half = data[0:n // 2]
    upper_half = data[n // 2 + 1:n]
    q1 = quartile(lower_half)
    q2 = quartile(data)
    q3 = quartile(upper_half)

print(q1)
print(q2)
print(q3)

# Using Statistics
# from statistics import median
#
# n = int(input())
# arr = [int(x) for x in input().split()]
# arr.sort()
# t = int(len(arr) / 2)
# if len(arr) % 2 == 0:
#     L = arr[:t]
#     U = arr[t:]
# else:
#     L = arr[:t]
#     U = arr[t + 1:]
#
# print(int(median(L)))
# print(int(median(arr)))
# print(int(median(U)))

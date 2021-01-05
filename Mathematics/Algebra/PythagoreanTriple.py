def pythagoreanTriple(a):
    if a % 2 == 0:
        b = (a // 2) ** 2 - 1
        c = b + 2
    else:
        b = (a ** 2 - 1) // 2
        c = b + 1
    return a, b, c


if __name__ == '__main__':
    a = int(input())

    triple = pythagoreanTriple(a)
    print(*triple)

    # Time Complexity: O(log a) or O(1)

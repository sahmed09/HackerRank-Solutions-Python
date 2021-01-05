def halloweenParty(k):
    if k % 2 == 0:
        result = k // 2
        result = result * result
    else:
        result = k // 2
        result = result * (result + 1)
    return result
    # return (k // 2) * (k // 2) + (k // 2) * (k % 2)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        k = int(input())
        result = halloweenParty(k)
        print(result)

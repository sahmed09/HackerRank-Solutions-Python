def sumOfGroup(k):
    # Return the sum of the elements of the k'th group.
    sum = 0
    temp = k * (k - 1) + 1  # calculates k'th groups first element
    for i in range(k):
        sum = sum + temp
        temp += 2
    return sum
    # return k ** 3


if __name__ == '__main__':
    k = int(input())

    answer = sumOfGroup(k)
    print(answer)

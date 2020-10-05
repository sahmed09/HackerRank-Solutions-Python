for i in range(1, int(input())):
    # print(str(i)*i)  # using string
    print((pow(10, i)//9) * i)  # using only math

    """
    10/9=1 * 1 = 1
    100/9=11 * 2 = 22
    .......
    """

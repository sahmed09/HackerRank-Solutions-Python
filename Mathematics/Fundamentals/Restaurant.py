import sys
import math


def restaurant(l, b):
    temp = math.gcd(l, b)
    return (l//temp) * (b//temp)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        lb = input().split()

        l = int(lb[0])
        b = int(lb[1])

        result = restaurant(l, b)
        print(result)

        # fptr.write(str(result) + '\n')
    # fptr.close()

"""
Time complexity: T*(log(l)+log(b)) 
Where
    T:number of test cases,   
    l : length of rectangle,  
    b: width of rectangle.
"""

import os

"""Pigeonhole Principle:
if N items are put into M containers, with N > M, then at least one container must contain more 
than one item.
if Jim removes N or fewer socks it is possible that all of those socks are of different colors. 
But if he removes N+1 or more socks, there must be at least two socks of the same color because 
there are only N different colors."""


def maximumDraws(n):
    return n + 1


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())
        result = maximumDraws(n)
        print(result)

        # fptr.write(str(result) + '\n')
    # fptr.close()
# Time Complexity: O(1)

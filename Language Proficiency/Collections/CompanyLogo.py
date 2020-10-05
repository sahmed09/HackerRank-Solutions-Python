from collections import Counter

if __name__ == '__main__':
    N = sorted(input())
    # print(N)

    # most_common() is used to produce a sequence of the n most frequently encountered input values and
    # their respective counts.

    counter = Counter(N).most_common(3)

    for i, j in counter:
        print(i, j)

    # for i in counter:
    #     print(*i)

# Another Approach using Counter:
"""from collections import Counter
from operator import itemgetter

for item in (sorted(sorted(Counter(input()).items()), key=itemgetter(1), reverse=True)[:3]):
    print(item[0], item[1])"""

# Normal Approach:
"""STEP 1: Create a list, letters, of size 26. Initialize each element to 0.
STEP 2: Traverse through the input string S. If a character in the string is 'a', then increment letter[0] 
    by 1. If 'b' is found, then increment letter[1] by 1 and so on.
STEP 3: Now run a loop three times. Inside the loop, store the maximum value of letters in the variable
    max_letter.
STEP 4:. In the scope of the previous loop, run another loop and find the index of the first occurrence 
    of max_letter. Now, print the appropriate letter associated with that index and the max_letter."""

"""S = input()
letters = [0] * 26

for letter in S:
    letters[ord(letter) - ord('a')] += 1

for _ in range(3):
    max_letter = max(letters)

    for index in range(26):
        if max_letter == letters[index]:
            print(chr(ord('a') + index), max_letter)
            letters[index] = -1
            break"""

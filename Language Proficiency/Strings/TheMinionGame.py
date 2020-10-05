def minion_game(string):
    s_length = len(string)
    vowel, consonant = 0, 0

    for i in range(s_length):
        if string[i] in "AEIOU":
            vowel = vowel + (s_length - i)  # (s-i) counts number of substrings can be made
            # for "BANANA" string[0]=B=consonant, total sub string = 6 (B, BA, BAN, BANA, BANAN, BANANA)
            # print("vowel", vowel)
        else:
            consonant = consonant + (s_length - i)
            # print("consonant", consonant)
            # for "BANANA" string[1]=A=consonant, total sub string = 6 (A, AN, ANA, ANAN, ANANA)

    if consonant > vowel:
        print("Stuart", consonant)
    elif consonant < vowel:
        print("Kevin", vowel)
    else:
        print("Draw")

    # if consonant > vowel:
    #     print(f"Stuart {consonant}")
    # elif vowel > consonant:
    #     print(f"Kevin {vowel}")
    # else:
    #     print("Draw")


if __name__ == '__main__':
    s = input().strip()
    minion_game(s)

"""
O(N) Solution:
If the string is BANANA, the substrings are:
B
BA
BAN
BANA
BANAN
BANANA
A
AN
ANA
ANAN
ANANA
N
NA
NAN
NANA
A
AN
ANA
N
NA
A
Words formed using the first letter B   = 6
Words formed using the second letter A  = 5
Words formed using the third letter N   = 4
Words formed using the fourth letter A  = 3
Words formed using the fifth letter N   = 2
Words formed using the last letter A    = 1
"""

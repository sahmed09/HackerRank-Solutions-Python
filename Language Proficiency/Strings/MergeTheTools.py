# from collections import OrderedDict
# def remove_duplicate(str1):
#     return "".join(OrderedDict.fromkeys(str1))
# print(remove_duplicate("Hellolllo"))
# print(remove_duplicate("Worldo"))

def merge_the_tools(string, k):
    count = 0
    s = ''

    for i in string:
        if i not in s:
            s += i
        count += 1

        if count == k:
            print(s)
            count = 0
            s = ''


# Another Approach:
def merge_the_tools_2(string, k):
    size = len(string) // k
    for index in range(size):
        # Subsegment string
        sub_string = string[index * k: (index + 1) * k]
        # print(sub_string)

        # Subsequence string having distinct characters
        u = ""

        # If a character is not already in 'u', append
        for c in sub_string:
            if c not in u:
                u += c

        # Print final converted string
        print(u)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    print()

    merge_the_tools_2(string, k)

    """
    The basic algorithm for solving this challenge is as follows:
    1.Divide string "s" into "len(s) // k" subsegments of length "k".
    2.Save the subsegment as variable "sub_string". For each "sub_string":
        Create a variable,"u", and initialize it to the empty string.
        Iterate over the characters in "sub_string" and append each character to "u" that does not already exist in "u".
        After iterating through all the characters in "sub_string", print the value of "u".
    """

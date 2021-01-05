def isBalanced(s):
    bracket_dict = {')': '(', ']': '[', '}': '{'}
    stack = []
    for x in s:
        if x in bracket_dict and stack and bracket_dict.get(x) == stack[-1]:
            # bracket_dict.get(x) similar to bracket_dict[x] -> both return the value for key
            stack.pop()
        else:
            stack.append(x)

    return "NO" if stack else "YES"


# def isBalanced(s):
#     n = -1
#     while len(s) != n:
#         n = len(s)
#         s = s.replace("()", "")
#         s = s.replace("[]", "")
#         s = s.replace("{}", "")
#
#     if len(s) == 0:
#         return "YES"
#     else:
#         return "NO"


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)
        print(result)

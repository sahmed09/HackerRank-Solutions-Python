import textwrap

# s = input()
# w = int(input())
# for _ in range(len(s)):
#     if len(s) > w:
#         print(s[:w])
#         s = s[w:]
#     else:
#         print(s)
#         break


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

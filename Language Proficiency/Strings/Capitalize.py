def solve(s):
    lists = []
    split_word = s.split(" ")
    # print(split_word)
    for word in split_word:
        lists.append(word.capitalize())
    output = " ".join(lists)
    return output


if __name__ == '__main__':
    s = "hello world"
    print(solve(s))

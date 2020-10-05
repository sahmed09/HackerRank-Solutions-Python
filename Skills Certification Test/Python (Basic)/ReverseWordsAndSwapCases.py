def reverse_words_order_and_swap_cases(sentence):
    words = sentence.split(" ")[::-1]
    return " ".join(words).swapcase()


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()
    result = reverse_words_order_and_swap_cases(sentence)
    print(result)

    # fptr.write(result + '\n')
    # fptr.close()

test = int(input())

my_string = ""
stack = []

for _ in range(test):
    operation = input().strip().split(" ")

    if operation[0] == "1":
        stack.append(my_string)
        my_string = my_string + operation[1]
    elif operation[0] == "2":
        stack.append(my_string)
        del_pos = int(operation[1])
        my_pos = len(my_string) - del_pos
        my_string = my_string[0:my_pos]
    elif operation[0] == "3":
        print_pos = int(operation[1]) - 1
        print(my_string[print_pos])
    else:
        my_string = stack.pop()
        # print(stack)
        # print(my_string)

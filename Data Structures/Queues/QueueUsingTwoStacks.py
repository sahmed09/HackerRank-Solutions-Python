# queue = []
#
# for i in range(int(input())):
#     query = list(map(int, input().split()))
#     if query[0] == 1:
#         queue.append(query[1])
#     elif query[0] == 2:
#         if len(queue) != 0:
#             queue.pop(0)
#     else:
#         print(queue[0])

# Using two stacks:
stack_in, stack_out = [], []

for i in range(int(input())):
    curr_inst = list(map(int, input().split(" ")))

    if curr_inst[0] == 1:
        stack_in.append(curr_inst[1])

    elif curr_inst[0] == 2:
        # If stack_out is not empty then pop from it
        if stack_out:
            stack_out.pop()
            continue
        else:
            # Move everything to the out stack:
            while stack_in:
                stack_out.append(stack_in.pop())
            stack_out.pop()
            continue

    else:
        if not stack_out:
            while stack_in:
                stack_out.append(stack_in.pop())
        print(stack_out[-1])

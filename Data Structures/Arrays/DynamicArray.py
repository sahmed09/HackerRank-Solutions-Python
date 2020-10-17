# Complete the 'dynamicArray' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries

def dynamicArray(n, queries):
    seq_list = [[] for _ in range(n)]
    last_ans = 0
    answer = []

    for query, x, y in queries:
        index = (x ^ last_ans) % n

        if query == 1:
            seq_list[index].append(y)
        else:
            position = y % len(seq_list[index])
            last_ans = seq_list[index][position]
            answer.append(last_ans)
    return answer


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])

    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)
    print(*result, sep="\n")

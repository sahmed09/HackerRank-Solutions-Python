def wrapper(f):
    def fun(l):
        f("+91 " + number[-10:-5] + " " + number[-5:] for number in l)
        # f("+91 {} {}".format(number[-10:-5], number[-5:]) for number in l)
        # f(map(lambda x: "+91 " + x[-10:-5] + " " + x[-5:], l))
    return fun

# def wrapper(f):
#     def fun(l):
#         decorated_l = ['+91 {} {}'.format(n[-10: -5], n[-5:]) for n in l]
#         return f(decorated_l)
#     return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)

# The any() function returns True if any item in an iterable are true, otherwise it returns False.
# If the iterable object is empty, the any() function will return False.
# When used on a dictionary, the any() function checks if any of the keys are true, not the values.

mytuple = (0, 1, False)
x = any(mytuple)
print(x)

myset = {0, 1, 0}
x = any(myset)
print(x)

mydict = {0: "Apple", 1: "Orange"}
x = any(mydict)
print(x)


if __name__ == '__main__':
    s = input()
    print(any([i.isalnum() for i in s]))
    print(any([i.isalpha() for i in s]))
    print(any([i.isdigit() for i in s]))
    print(any([i.islower() for i in s]))
    print(any([i.isupper() for i in s]))

import os
from datetime import datetime


# Complete the time_delta function below.
def time_delta(t1, t2):
    time_format = "%a %d %b %Y %H:%M:%S %z"  # UTC offset
    # Using strptime we can get a time object.
    # strptime() parses a string representing a time according to a format.
    t1 = datetime.strptime(t1, time_format)
    t2 = datetime.strptime(t2, time_format)
    return str(int(abs(t1 - t2).total_seconds()))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)
        print(delta)

        # fptr.write(delta + '\n')
    # fptr.close()

# Without Function:
# our goal is the first convert the time stamp to UNIX time stamps that are independent of timezones.
# After that we simply subtract and print the difference.
time_format = '%a %d %b %Y %H:%M:%S %z'
for i in range(int(input())):
    t1 = datetime.strptime(input(), time_format)
    t2 = datetime.strptime(input(), time_format)
    print(abs(int((t1-t2).total_seconds())))

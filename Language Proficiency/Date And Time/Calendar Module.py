import calendar

month, day, year = map(int, input().split())

weekday = calendar.weekday(year, month, day)

if weekday == 0:
    print("MONDAY")
elif weekday == 1:
    print("TUESDAY")
elif weekday == 2:
    print("WEDNESDAY")
elif weekday == 3:
    print("THURSDAY")
elif weekday == 4:
    print("FRIDAY")
elif weekday == 5:
    print("SATURDAY")
elif weekday == 6:
    print("SUNDAY")

"""day = {0: 'MONDAY', 1: 'TUESDAY', 2: 'WEDNESDAY', 3: 'THURSDAY', 4: 'FRIDAY', 5: 'SATURDAY', 6: 'SUNDAY'}
m, d, y = map(int, input().split())
print(day[calendar.weekday(y, m, d)])"""

"""m, d, y = map(int, input().split())
print((calendar.day_name[calendar.weekday(y, m, d)]).upper())"""

# print(calendar.TextCalendar(firstweekday=6).formatyear(2015))

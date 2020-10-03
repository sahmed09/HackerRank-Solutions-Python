return_day, return_month, return_year = map(int, input().split())
expected_day, expected_month, expected_year = map(int, input().split())

if (return_year, return_month, return_day) <= (expected_year, expected_month, expected_day):
    print(0)
elif (return_year, return_month) == (expected_year, expected_month):
    print(15 * (return_day - expected_day))
elif return_year == expected_year:
    print(500 * (return_month - expected_month))
else:
    print(10000)

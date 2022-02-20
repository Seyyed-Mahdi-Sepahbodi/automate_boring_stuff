import re

dateDetectionRegex = re.compile(r'''(
    (0[1-9]|[1-2][0-9]|3[0-1])
    /
    (0[1-9]|1[0-2])
    /
    ([1-2]\d{3})
    )''', re.VERBOSE)

date = input("Please enter date in DD/MM/YYYY format: ")

result = dateDetectionRegex.search(date)

month_with_30_days = (4, 6, 9, 11)
month_with_31_days = (1, 3, 5, 7, 8, 10, 12)

if result == None:
    print('Wrong')
else:
    date_groups_tuple = result.groups()
    day = int(date_groups_tuple[1])
    month = int(date_groups_tuple[2])
    year = int(date_groups_tuple[3])
    if month in month_with_30_days:
        if day > 30:
            print('Wrong')
    elif month in month_with_31_days:
        if day > 31:
            print('Wrong')
    else:
        if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
            if day > 29:
                print('Wrong')
        else:
            if day > 28:
                print('Wrong')
    
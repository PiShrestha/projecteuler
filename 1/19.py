# is leap year

def isLeap(year: int) -> bool:
    if (year % 4 == 0 and not (year % 100 == 0)) or year % 400 == 0:
        return True

    return False

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# loop year -> month
curr_day = 1
count = 0

for year in range(1900, 2001):
    for month in range(12):
        print(month, year, curr_day)
        if month == 1 and isLeap(year):
            remainder = (days[month] + 1) % 7 # add one day for february on leap year
        else:
            remainder = days[month] % 7 # offset

        curr_day = (curr_day + remainder) % 7
        if curr_day == 0 and year != 1900:
            count += 1

print(count)

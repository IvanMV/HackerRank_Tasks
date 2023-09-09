import calendar

data = tuple(map(int, input().split()))
day = calendar.weekday(data[2], data[0], data[1])
print(calendar.day_name[day].upper())
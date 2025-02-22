import calendar

year = int(input("Enter the year: "))
# month = int(input("Enter the month: "))
# To print entire year
# print(calendar.calendar(year))

for i in range(1, 13):
    print(calendar.month(year, i))

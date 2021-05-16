# Exercise 3

# Import related libraries
from datetime import datetime, timedelta


# Define generator for date of input week
def weekday_gen(s_date: datetime, e_date: datetime, w_day: int):
    print("Start")

    diff_week = w_day - s_date.weekday()
    temp_date = datetime(year=s_date.year, month=s_date.month, day=(s_date.day + diff_week))
    if temp_date >= s_date:
        yield temp_date

    while temp_date <= e_date:
        temp_date = temp_date + timedelta(days=7)
        if temp_date > e_date:
            print("End")
            break
        yield temp_date


# Example
t1 = datetime(year=1399, month=12, day=12)
t2 = datetime(year=1400, month=11, day=17)
for i in weekday_gen(t1, t2, 1):
    print(i)

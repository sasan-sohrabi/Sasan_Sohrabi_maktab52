# Exercise 2

# Import related library
from datetime import datetime
import jdatetime

print(15 * "-", "Date Program-", 15 * "-", "\n")


# first_date = input("-> Please Enter your first date (format:yyyy/mm/dd hh:mm:ss):\n")
# second_date = input("-> Please Enter your first date (format:yyyy/mm/dd hh:mm:ss):\n")


def date_input(which_date: str) -> dict:
    # Description of program
    print(f"-> Please Enter your {which_date} date step by step.\n1-year\n2-month\n3-day\n4-hour\n5-minute\n6-second\n")

    # date_dic is contain input date
    date_dic = {}

    # Define Valid date function for check is input date is correct or not.
    def is_valid_date(year_in: int, month_in: int, day_in: int) -> bool:
        correctDate = None
        try:
            date = datetime(year=year_in, month=month_in, day=day_in)
            correctDate = True
        except ValueError:
            correctDate = False
        return correctDate

    # Year of date
    while True:
        try:
            year = int(input("-> Enter year (must be integer and positive):"))
            if year < 0:
                raise ValueError('Year must be positive')
            date_dic['Year'] = year
            break
        except ValueError as e:
            print(e)
            continue

    # Month of date
    while True:
        try:
            month = int(input("-> Enter month (must be integer and between 1 to 12):"))
            if not 1 <= month <= 12:
                raise ValueError("month must be between 1 to 12")
            date_dic['Month'] = month
            break
        except ValueError as e:
            print(e)
            continue

    # Day of date
    while True:
        try:
            day = int(input("-> Enter day (must be integer and between 1 to 30):"))
            # if not 1 <= day <= 30:
            #     raise ValueError("Day must be between 1 to 30")
            if not is_valid_date(date_dic['Year'], date_dic['Month'], day):
                raise ValueError('Day is not valid')
            date_dic['Day'] = day
            break
        except ValueError as e:
            print(e)
            continue

    # Hour of date
    while True:
        try:
            hour = int(input("-> Enter hour (must be integer and between 0 to 23):"))
            if not 0 <= hour <= 23:
                raise ValueError("Hour must be between 0 to 23")
            date_dic['Hour'] = hour
            break
        except ValueError as e:
            print(e)
            continue

    # Minute of date
    while True:
        try:
            minute = int(input("-> Enter Minute (must be integer and between 0 to 59):"))
            if not 0 <= minute <= 59:
                raise ValueError("Minute must be between 0 to 59")
            date_dic['Minute'] = minute
            break
        except ValueError as e:
            print(e)
            continue

    # Second of date
    while True:
        try:
            second = int(input("-> Enter second (must be integer and between 0 to 59):"))
            if not 0 <= second <= 59:
                raise ValueError("second must be between 0 to 59")
            date_dic['Second'] = second
            break
        except ValueError as e:
            print(e)
            continue

    print(f"{which_date} date without any problem saved."
          f"\n{which_date} : {date_dic['Year']}/{date_dic['Month']}/{date_dic['Day']}"
          f" {date_dic['Hour']}:{date_dic['Minute']}:{date_dic['Second']}")

    return date_dic


# Define main function for running programme
def main() -> None:
    # Input first and second date
    first = date_input('first')
    second = date_input('second')

    # Convert input dates to datetime format
    t1 = datetime(year=first['Year'], month=first['Month'], day=first['Day'],
                  hour=first['Hour'], minute=first['Minute'], second=first['Second'])
    t2 = datetime(year=second['Year'], month=second['Month'], day=second['Day'],
                  hour=second['Hour'], minute=second['Minute'], second=second['Second'])

    # Part 1 - Difference between to date in seconds
    print("Difference between to date in seconds is : ", (t2 - t1).total_seconds())

    # Part 2 - Count of leap year between two input date

    def leap_year(start_year: int, end_year: int) -> int:
        leap_year_list = []
        while start_year <= end_year:
            if start_year % 4 == 0:
                if start_year % 100 == 0:
                    if start_year % 400 == 0:
                        leap_year_list.append(start_year)
                else:
                    leap_year_list.append(start_year)
            start_year += 1
        return len(leap_year_list)

    print("Count of leap year between two input date is :", leap_year(t1.year, t2.year))

    # Part 3 - Gregorian date to jalali date
    first_jalali = jdatetime.date.fromgregorian(year=first['Year'], month=first['Month'], day=first['Day'])
    second_jalali = jdatetime.date.fromgregorian(year=second['Year'], month=second['Month'], day=second['Day'])
    print(f"First Input gregorian date is {t1} and jalali date is ", first_jalali)
    print(f"Second Input gregorian date is {t2} and jalali date is ", second_jalali)


main()

# gregorian_date =  jdatetime.date.fromgregorian(day=24 ,month=3,year=2020)
# print(gregorian_date)

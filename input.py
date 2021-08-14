input_day = int(input("Day? "))
input_month = int(input("Month? "))
input_year = int(input("Year? "))

if input_year < 1900 or input_year > 2020:
    print("Invalid year")

if input_month < 1 or input_month > 12:
    print("Invalid month")

if input_month == 2 and input_day > 28:
    print("Invalid day")

if input_month in (4, 6, 9, 11) and input_day > 30:
    print("Invalid day")

else:
    if input_day > 31:
        print("Invalid day")

from Calculation_age import get_data

birthday_day = int(input('Enter your birthday day: '))
birthday_month = int(input('Enter your birthday month: '))
birthday_year = int(input('Enter your birthday year: '))

if 0<birthday_day<31 and 0<birthday_month<13 and 0<birthday_year:
    year,month,day = get_data(birthday_day,birthday_month,birthday_year)
    print(f'Your age is {day} days and {month} month and {year} years ')
else:
    print('Your input wrong number')

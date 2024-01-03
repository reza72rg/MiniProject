from Calculation_age import get_data

try:
    birthday_day = int(input('Enter your birthday day (1-31): '))
    if not 1 <= birthday_day <= 31:
        raise ValueError("Invalid day input")

    birthday_month = int(input('Enter your birthday month (1-12): '))
    if not 1 <= birthday_month <= 12:
        raise ValueError("Invalid month input")

    birthday_year = int(input('Enter your birthday year: '))
    if birthday_year < 0:
        raise ValueError("Invalid year input")

    year, month, day = get_data(birthday_day, birthday_month, birthday_year)
    print(f'Your age is {day} days, {month} months, and {year} years.')
except ValueError as e:
    print(f'Error: {str(e)}')

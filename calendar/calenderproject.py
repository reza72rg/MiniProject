from datetime import datetime
import calendar
year= datetime.now().year
month= datetime.now().month
x= calendar.month(year, month)
print(f"The calendar of This Month is : {x}") 
print(f"The calendar of year 2024 is : {calendar.calendar(year)}") 


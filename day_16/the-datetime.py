#Exercises: Day 16
#1. Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime, date
now = datetime.now()
current_day = now.day
current_month = now.month
current_year = now.year
current_hour = now.hour
current_minute = now.minute
current_timestamp = now.timestamp()

print(f'Day: {current_day}, Month: {current_month}, Year: {current_year}, Hour: {current_hour}, Timestamp: {current_timestamp}')

#2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S"
current_day_format = now.strftime("%m/%d/%Y, %H:%M:%S")
print(current_day_format)

#3. Today is 5 December, 2019. Change this time string to time.
date_string = "5 December, 2019"
date_time = datetime.strptime(date_string, "%d %B, %Y")
print(date_time)

#4. Calculate the time difference between now and new year.
now = date(year=2025, month=7, day=15)
new_year = date(year=2017, month=1, day=1)
difference_between = now - new_year
print(now)
print(new_year)
print(f'the time difference between now and new year is: {difference_between}')

#5. Calculate the time difference between 1 January 1970 and now.
now = date(year=2025, month=7, day=15)
seconde_date = date(year=1970, month=1, day=1)
difference_now_seconde = now - seconde_date
print(difference_now_seconde)
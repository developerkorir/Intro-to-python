from datetime import date, datetime, timedelta

# print out today's data
today = date.today()
print(today)

dt = datetime.now()
print(dt)

formatted_date = today.strftime(f"%a, %d %B %Y")
print(formatted_date)

# check date from the past or future
_33days_ago = today-timedelta(days=33)
print(_33days_ago)

_180_days_future = today+timedelta(days=180)
print(_180_days_future)

# get date from string to date
date_string = "07 April 2000"
date_object = datetime.strptime(date_string, "%d %B %Y")
print(date_object)



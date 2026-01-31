# Day 16: 30 Days of python programming

from datetime import date, datetime, timedelta
import time

today_date = datetime.today()
today_year = today_date.year
today_month = today_date.month
today_day = today_date.day
today_hour = today_date.hour
today_minute = today_date.minute
today_seconde = today_date.second
today_timestamp = today_date.timestamp()

format_date = today_date.strftime("%m/%d/%Y, %H:%M:%S")
convert_date = datetime.strptime("5 December, 2019", "%d %B, %Y")
date_yesterday = today_date - timedelta(days=1)
date_diff = date(year=1970, month=1, day=1) - today_date.date()

start = time.perf_counter()
print("Today : ", today_date.date())
print("Formating : ", format_date)
print("Convert date : ", convert_date)
print("Yesterday : ", date_yesterday)
print("Difference date : ", date_diff)
end = time.perf_counter()

print(f"Execution time : {end - start:.6f} ")

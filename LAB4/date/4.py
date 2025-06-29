from datetime import datetime
date_str = '18-02-2015 20:50:00'
day = int(date_str[0:2])
month = int(date_str[3:5])
year = int(date_str[6:10])
hour = int(date_str[11:13])
minute = int(date_str[14:16])
second = int(date_str[17:19])
date1 = datetime(year, month, day, hour, minute, second)
date2 = datetime.now()
difference = (date2 - date1).total_seconds()
print(difference)



















'''difference_in_years = difference / (365.25 * 86400)
print(f"Difference in years: {difference_in_years}")
'''
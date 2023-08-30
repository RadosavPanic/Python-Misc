# Date and Time

import time
import calendar

print(f'Ticks since 1.1.1970: {time.time()}')  # 1693395486.971545

# ----TIME CREATION----

# tuple_time = (yyyy, m, d, hour, min, sec, weekday, yearday, isdst, timezone)
tupleTime = (2023, 8, 30, 16, 18, 26, 1, 241, 0)
time_created = time.mktime(tupleTime)  # mktime(secs) -> float
print(time.asctime(time.localtime(time_created)))  # Wed Aug 30 17:18:26 2023

print(f"Old time: {time.ctime()}")  # Old time: Wed Aug 30 17:35:01 2023
print("Sleeping.... (2s)")
time.sleep(2)
print(f"New time (2s timelapse): {time.ctime()}")  # New time (2s timelapse): Wed Aug 30 17:35:04 2023

# ----TUPLE STRUCT_TIME----

print(f'Local current time: {time.localtime(time.time())}')  # time.struct_time(tm_year=2023, tm_mon=8,
# tm_mday=30, tm_hour=13, tm_min=40, tm_sec=48, tm_wday=2, tm_yday=242, tm_isdst=1)
print(time.gmtime())  # same as above
print(calendar.timegm(tupleTime))  # 1693412306 (opposite of gmtime, takes tuple and returns secs since 1.1.1970)

# ----TUPLE CURRENT TIME----

print(f"Formatted current time: {time.asctime(time.localtime(time.time()))}")  # Wed Aug 30 13:42:39 2023
print(time.asctime(time.localtime()))  # same as above, localtime secs arg returns current time if None passed
print(time.ctime())  # same as above

# ----TIME FORMATTING----

print(time.strftime("%d-%b-%Y %H:%Mh", time.gmtime(time_created)))  # 30-Aug-2023 15:18h
print(time.strptime("15 August 22", "%d %B %y"))  # time.struct_time(tm_year=2022,
# tm_mon=8, tm_mday=15, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=227, tm_isdst=-1)

# ----TIMEZONE----

print(f"Offset of local DST timezone west of UTC (secs): {time.altzone}")  # -7200 (only use if daylight is nonzero)
print(f"Offset without DST (>0 America, <= 0 Europe/Asia/Africa): {time.timezone}")  # -3600
print("Tuple(non-DST & DST)", time.tzname)  # ('Central Europe Standard Time', 'Central Europe Daylight Time')

# ----CALENDAR MODULE----

# ----YEAR----

# calendar.calendar(year,w,l,c) & calendar.prcal(year,w,l,c) -> 3-column calendar for whole year (multi-line str)

# ----MONTH----

print(calendar.month(2023, 8))
"""
    August 2023
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31
"""

print(calendar.month(2023, 8, 5, 1)) # also calendar.prmonth(year,month,w,l)
"""
               August 2023
 Mon   Tue   Wed   Thu   Fri   Sat   Sun
         1     2     3     4     5     6
   7     8     9    10    11    12    13
  14    15    16    17    18    19    20
  21    22    23    24    25    26    27
  28    29    30    31
"""

print(calendar.monthcalendar(2023, 8))  # 1-sub_list = 1 week (int=0 if weekday isn't in current month)
""" [[0, 1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12, 13], [14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27], 
[28, 29, 30, 31, 0, 0, 0]]
"""

print(calendar.monthrange(2023, 8))  # (1, 31) (firstDayIndex, numberOfDaysInMonth)

# ----LEAP----

print(calendar.leapdays(2024, 2029))  # 2 (number of leap days between in range of 2 passed year args)
print(calendar.isleap(2024))  # True (False for non-leap, True for leap years)

# ----WEEK----

print(calendar.firstweekday())  # 0 (Monday, 0-based)
calendar.setfirstweekday(1); print(calendar.firstweekday())  # 1

print(calendar.weekday(2023, 8, 30))  # 2 (0-based, 2 = Wednesday)






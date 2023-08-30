# Date and Time

import time

print(f'Ticks since 1.1.1970: {time.time()}')  # 1693395486.971545
print(f'Local current time: {time.localtime(time.time())}')  # time.struct_time(tm_year=2023, tm_mon=8,
# tm_mday=30, tm_hour=13, tm_min=40, tm_sec=48, tm_wday=2, tm_yday=242, tm_isdst=1)

print(f'Local offset DST zone: {time.altzone}')  # -7200

print(f"Formatted current time: {time.asctime(time.localtime(time.time()))}")  # Wed Aug 30 13:42:39 2023
print(time.asctime(time.localtime()))  # same as above, localtime secs arg returns current time if None passed
print(time.ctime())  # same as above






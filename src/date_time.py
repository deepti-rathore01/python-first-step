"""
@file : date_time.py
@file :print the dates between March-2017 to April-2017 using datetime
"""
from datetime import date, timedelta
d1 = date(2017,3,1)
d2 = date(2017, 4,  30)
delta = d2 - d1
for loop in range(delta.days+1):
        print(d1 + timedelta(days=loop))





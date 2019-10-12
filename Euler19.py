#Euler 19

import datetime
year = 1901
month = 1
day = 1
counter = 0

while year < 2001:
    while month < 13:
        date = datetime.datetime(year, month, day)
        x = datetime.datetime.weekday(date)
        if x == 6:
            counter = counter + 1
        month = month + 1
    year = year + 1
    month = 1
print(counter)

#date = datetime.datetime(year, month, day)
#x = datetime.datetime.weekday(date)
#print(x)



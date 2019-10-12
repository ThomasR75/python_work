# find the longest recurring cycle in the decimals for 1/x for x<1000
from decimal import *
getcontext().prec = 5000
x = Decimal(1)
o = 1
number = 1
while x < 1000:
    c = 1 / x
    print(c)
    z = str(c)
    #print(len(z))
    d = list(z[2:])
    while len(d) < 50:
        d.append('0')
    e = 10
    l = 1
    while d[e:e+l] != d[e+l:e+l+l] and e < 100:
        while d[e:e+l] != d[e+l:e+l+l] and l < 5000:
            l = l + 1
        e = e + 1
    print(d[e:e+l])
    if l > o:
        o = l
        number = x
    print(d)

    x += 1
print(o)
print(number)
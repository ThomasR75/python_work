#Euler39 Perimeter of right angle triangle <1000

import math
a = 1
b = 1
c = 0
p = 1000
list = []
large = []
while p > 1:
    while a < 500:
        while b < 500:
            c = math.sqrt(a**2 + b**2)
            if c % 1 == 0:
                if a + b +c == p:
                    list.append(a)
                    list.append(b)
                    list.append(c)
            b = b + 1
        b = 1
        a = a + 1
    if len(list) > len(large):
        large = list
    a = 1
    list = []
    p -= 1
print (large)
print (len(large))
print (len(set(large)))
#Euler 56
from time import time
start = time()
a = 0
b = 0
c_digit = 0
c_digitmax = 0
while a < 101:
    b = 0
    while b < 101:
        c_digit = 0
        c = a ** b
        #print(a, b, c)
        for i in str(c):
            c_digit = c_digit + int(i)
        if c_digit > c_digitmax:
            c_digitmax = c_digit
        b += 1
    a += 1
print(c_digitmax)
end = time()
print("Time:", end - start)
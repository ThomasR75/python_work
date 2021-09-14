# Euler 57 Square root convergents

from time import time
start = time()
# start iterator
num = 1
denom = 1
counter = 1
# first iteration using algo a(1) = a(0)/2 + 1/a(0)
# to stay in fractions expressed as below
# num1 = num; denom1 = denom * 2
# num2 = denom, denom2 = num
while counter < 10:

    num1 = num
    denom1 = denom * 2
    num2 = denom
    denom2 = num

#compare denominators and equalize
    if denom2 == denom1:
        denom3 = denom2
        num3 = num2 + num1

    else:
        denom3 = denom2 * denom1
        num3 = (num1 * denom2) + (num2 * denom1)

    print (num3)
    print (denom3)
    print("------------")
    counter += 1
    num = num3
    denom = denom3
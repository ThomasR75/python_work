# Euler 57 Square root convergents

from time import time
start = time()
# start iterator
num = 1
denom = 1
num1 = 2
denom1 = 1
num2 = 1
denom2 = 2
counter = 2
important = 0
# start iteration from bottom and move up
while counter < 1001:

    if denom2 == denom1:
        denom3 = denom2
        num3 = num1 + num2
    else:
        denom3 = denom2 * denom1
        num3 = (num1 * denom2) + (num2 * denom1)

    nnum3 = denom3
    ddenom3 = num3
    num2 = nnum3
    denom2 = ddenom3
    numerator = nnum3 + ddenom3
    denominator = ddenom3
    if len(str(numerator)) > len(str(denominator)):
        important += 1
    print(numerator)
    print(denominator)
    print(important)
    print("----------")
    counter += 1
end = time()
print("Time", end-start)
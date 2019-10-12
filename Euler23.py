# Euler23 non-abundant sums
# all numbers>28123 are sum of two abundant numbers
# which numbers below cannot be expressed using two abundant numbers?
# sum those up
# 1. determine all abundant numbers to that limit

# finding abundant numbers, by finding proper divisors and summing them. if larger than number = abundant numbers

a = 1
d = 1
b = 28123
divisorsum = 0
divisors = []
abundant = []
total = 0
summe = 0
while a < b:
    while d < a:
        if a % d == 0:
            divisors.append(d)
        d += 1
    for i in divisors:
        divisorsum += i
    if divisorsum > a:
        abundant.append(a)
    divisorsum = 0
    divisors = []
    d = 1
    a = a + 1
# print(abundant)
abundant_set = set(abundant)
for i in range (1, 28123):
    for k in abundant:
        if i - k in abundant_set:
            total += i
            break
for i in range (1, 28123):
    summe = summe + i
print(summe)
print(total)
diff = summe - total
print(diff)



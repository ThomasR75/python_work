# Euler 34; Digit Factorials
import math
start = 900000
sum_digits = 0
number_sum = 0

while start > 2:
    for i in str(start):
        sum_digits = sum_digits + math.factorial(int(i))
    if sum_digits == start:
        number_sum = number_sum + start
    sum_digits = 0
    start = start - 1
print(number_sum)
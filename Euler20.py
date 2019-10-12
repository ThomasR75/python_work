# Euler20 Factorial Sums
import math
x = math.factorial(100)
print(x)

def sum_digits(x):
    s = 0
    while x:
        s += x % 10
        x //= 10
    return s

print(sum_digits(x))
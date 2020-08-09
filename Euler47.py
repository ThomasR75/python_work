#Euler47
#consecutive numbers with same digit prime factors
from time import time
#create list of primes
primemax = 100000
marked = [0] * primemax
primes = [2, ]
value = 3

while value < primemax:
    if marked[value] == 0:
        primes.append(value)
        i = value
        while i < primemax:
            marked[i] = 1
            i += value
    value += 2
#parameters
begin = time()
start1 = 132000
div = 2
step = 0
#find prime factors
factors = []
integers = []
while start1 < 135000:
    start = start1
    while div < start1:
        step = start / div
        if step.is_integer():
            factors.append(div)
            start = step
        else:
            if div > 2:
                div += 2
            else:
                div += 1
    factorset = set(factors)
    if len (list (factorset)) == 4:
        integers.append(start1)

    div = 2
    start1 += 1
    factors = []
count = len(integers)
x = 0
while x < count-3:
    if integers[x] * 3 == integers[x+1] + integers[x+2] + integers[x+3] - 6:
            #if integers[x] == integers[x+3] - 3:
                print (integers[x])
                x += 1
    else:
        x += 1
end = time()
print("Time", end-begin)
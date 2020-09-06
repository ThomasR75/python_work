#Euler50 consecutive prime sum
#largest sum of a consecutive primes below 1mio

#list of primes
from time import time
begin = time()
primemax = 100
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
print (primes)
sum = 2
x = 1

print (sum)


end = time()
print("Time: ", end-begin)

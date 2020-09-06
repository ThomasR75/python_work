#create list of primes
from time import time
begin = time()
primemax = 10000
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
#print (primes)
x = primes.index(1009)
fourdigitprimes = primes[x:]

count = len(fourdigitprimes)
print(count)
x = 1
y = 0
while y < count:
    while x < count:
        one = str(fourdigitprimes[y])
        two = str(fourdigitprimes[x])


        newnumber = fourdigitprimes[x] + fourdigitprimes[x] - fourdigitprimes[y]

        x += 1



end = time()
print("Time", end-begin)
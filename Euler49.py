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

print(fourdigitprimes)
#print(len(fourdigitprimes))

reducedprimes = []
from itertools import permutations
for i in fourdigitprimes:
    l = list(permutations(str(i)))
    numlist = []
    for k in l:

        num = ''
        for o in k:
            num = num + o
        num = int(num)
        if num in fourdigitprimes and num not in numlist:
            numlist.append(num)
        num1 = 0
        #print(numlist)

        if num in fourdigitprimes and num > i:
            step = num - i
            num1 = num + step
            #print(numlist)
        if num1 in fourdigitprimes and num1 in numlist:
            reducedprimes.append(i)
            reducedprimes.append(num)
            reducedprimes.append(num1)
print(reducedprimes)
end = time()
print("Time", end-begin)
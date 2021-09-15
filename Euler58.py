# Euler 58 spiral primes

from time import time
starttime = time()

#Generate Primes using fast sieve

primemax = 300000
marked = [0] * primemax
primes = [2]
value = 3
s = 2
while value < primemax:
    if marked[value] == 0:
        s += value
        primes.append(value)
        i = value
        while i < primemax:
            marked[i] = 1
            i += value
    value += 2
#print(primes)

#Create Spiral numbers and check if prime
start = 1
step = 2
counter = 1
loop = 1
ratio = 1
isprime = 0
isprimelist = []
noprime = 1
noprimelist = []
#while loop < 4:
while ratio > 0.10:
    while counter < 5:
        start = start + step
        if start in primes:
            isprime += 1
            isprimelist.append(start)
        else:
            noprime += 1
            noprimelist.append(start)
        counter += 1

    step += 2
    loop += 1
    counter = 1
    ratio = isprime / (isprime + noprime)
print(isprime)
print(isprimelist)
print(noprime)
print(noprimelist)
print(ratio)
print(loop)
print(start)
end = time()
print ("Time:", end-starttime)
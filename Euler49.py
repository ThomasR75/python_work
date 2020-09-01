#create list of primes
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
fourdigitprimes = []
fourdigitprimes = primes[x:]

#print(fourdigitprimes)
#print(len(fourdigitprimes))
cleanedprimes = []
for i in fourdigitprimes:
    j = ''.join(set(str(i)))
    if len(j) == 4:
        cleanedprimes.append(i)
print(cleanedprimes)
print(len(cleanedprimes))

#Euler 37 find 11 truncable Primes from left and right

# Create Primes below 1mio
primemax = 1000000
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
print(len(primes))

#check if right truncation is prime
rprimes = []
for x in primes[4:]:
    digits = len(str(x))
    counter = 0
    if digits > 1:
        cut = 1
        while cut <= digits-1:
            y = int(str(x)[:digits-cut])
            if y in primes:
                counter += 1
            if counter == digits-1:
                 rprimes.append(x)
            cut += 1
print(rprimes)
print(len(rprimes))

#check if left truncation is prime
lprimes = []
for x in rprimes:
    digits = len(str(x))
    counter = 0
    if digits > 1:
        cut = 1
        while cut <= digits-1:
            y = int(str(x)[cut:])
            if y in primes:
                counter += 1
            if counter == digits-1:
                 lprimes.append(x)
            cut += 1
print(lprimes)
print(len(lprimes))

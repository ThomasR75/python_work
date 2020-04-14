#Euler 41 find largets pandigital Prime

#create list of primes
# Create Primes below sqrt(987654321) as divisors to test if pandigital is prime
primemax = 31427
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

x = 1423
for i in primes:
    if i < x:
        z = x % i
        print (i)
        print (z)

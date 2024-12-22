#Euler 60 Prime pair sets

from itertools import combinations

#Create primes with fast sieve
primemax = 99000
marked = [0] * primemax
primes = []
value = 3
while value < primemax:
    if marked[value] == 0:
        primes.append(value)
        i = value
        while i < primemax:
            marked[i] = 1
            i += value
    value += 2

#take first prime and second prime
numbers = [primes[0], primes[1], primes[2], primes[3]]

while True:
    prime_set = set(numbers)
    print("Checking number", numbers)

    if all(int(str(a) + str(b)) in primes and int(str(b) + str(a)) in primes for a, b in combinations(prime_set, 2)):
        print(numbers)
        break

    i = len(numbers) - 1
    while i >= 0:
        if numbers[i] < primes[-1]:
            numbers[i] = primes[primes.index(numbers[i]) + 1]
            break
        else:
            numbers[i] = primes[primes.index(numbers[i-1]) + 2]
            i -= 1
            if i < 0:
                break

print("Not prime")
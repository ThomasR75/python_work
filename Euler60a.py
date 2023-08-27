#Euler 60 Prime pair sets

from itertools import combinations

#Create primes with fast sieve
primemax = 999000
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
first = 0
second = 1
third = 2
p1 = primes[first]
p2 = primes[second]
p3 = primes[third]
numbers = [p1,p2, p3]

while True:
    prime_set = set(numbers)
    print("Checking number", numbers)

    if all(int(str(a) + str(b)) in primes and int(str(b) + str(a)) in primes for a, b
                                                 in combinations(numbers,2)):
        print(numbers)
        break
    for i in range(len(numbers)-1, -1, -1):
        if numbers[i] == primes[-1]:
            break
        numbers[i] = primes[primes.index(numbers[i]) + 1]
        numbers[i+1:] = primes[:i+1]
        break
    else:
        break

print ("not prime")

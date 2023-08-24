#Euler 60 Prime pair sets

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
second = 2
third = 4
p1 = primes[first]
p2 = primes[second]
p3 = primes[third]
numbers = [p1,p2,p3]
sum = 3
while sum in primes:
    for i in numbers:
        for j in numbers:
            if i != j:
                sum = int(str(i)+str(j))
                if sum not in primes:
                    print (str(sum) + " no prime")
                    break
                else:
                    print (sum)
else:
    print ("not prime")

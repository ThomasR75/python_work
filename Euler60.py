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
third = 3
p1 = primes[first]
p2 = primes[second]
p3 = primes[third]
numbers = [p1,p2,p3]
num_sum = 3
while num_sum in primes:
    for i in numbers:
        for j in numbers:
            if i != j:
                num_sum = int(str(i)+str(j))
                if num_sum not in primes:
                    print (str(num_sum) + " no prime")
                    break
                else:
                    print (num_sum)
        else:
            continue
        break
    else:
        break
else:
    print ("not prime")

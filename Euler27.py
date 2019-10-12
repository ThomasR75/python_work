# Euler 27 quadratic primes
# create a list of primes and check for each number if its in the list.
# break at first when not in list and try next. keep counter

# create first 10,000 primes

primes = set([2])
value = 3
while len(primes) < 1000:
    isPrime = True
    for k in primes:
        if value % k == 0:
            value += 2
            isPrime = False
            break
    if isPrime:
        primes.add(value)
        value += 2

# run process and check if result is in list
n = 0
a = -999
b = -1000
counter = 0
max = 1
while a < 1000:
    while b < 1001:
        while n < 100:
            p = n*n + a*n + b
            if p in primes:
                counter += 1
                if counter > max:
                    max = counter
                if counter == 71:
                     print ("a =" + str(a))
                     print ("b =" + str(b))
                     print (p)
                     print(a*b)
            n += 1
            if p not in primes:
                break
        counter = 0
        n = 0
        b += 1
    n = 0
    b = -1000
    a += 1
print(max)

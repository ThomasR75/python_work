primemax = 3000
marked = [0] * primemax
primes = []
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
print (s)
print (primes)

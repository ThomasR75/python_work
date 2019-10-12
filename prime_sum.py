#sum of 2mio primes
def eratosthenes(n):
    multiples = []
    primesum =0
    for i in range(2, n+1):
        if i not in multiples:
            primesum = primesum + i
            for j in range(i*i, n+1, i):
                multiples.append(j)
    print(primesum)
	
                			
eratosthenes(1000)

def eratosthenes(n):
    multiples = []
    primes = []
    #x = 1
    for i in range(2, n+1):
        while i < n:
			if i not in multiples:
				print (i)
				#print(x)
				primes.append(i)
				#x = len(primes) + 1
				for j in range(i*i, n+1, i):
					multiples.append(j)
	print (i)	
eratosthenes(1000)


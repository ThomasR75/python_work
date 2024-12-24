#Euler 60 Prime pair sets

def miller_rabin(n, k=3):
    """Miller-Rabin primality test
    n: number to test
    k: number of rounds (higher k means more accurate but slower)
    """
    import random
    
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0: return False

    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randrange(2, n-1)
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(r-1):
            x = (x * x) % n
            if x == n-1:
                break
        else:
            return False
    return True


import time
start_time = time.time()

#Create primes with fast sieve
primemax = 10000
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


for p1 in primes:
    index1 = primes.index(p1)
    for p2 in primes[index1+1:]:
        index2 = primes.index(p2)
        if miller_rabin(int(str(p1)+str(p2))):
            if miller_rabin(int(str(p2)+str(p1))):
                for p3 in primes[index2+1:]:
                    index3 = primes.index(p3)
                    if miller_rabin(int(str(p1)+str(p3))):
                        if miller_rabin(int(str(p3)+str(p1))):
                            if miller_rabin(int(str(p2)+str(p3))):
                                if miller_rabin(int(str(p3)+str(p2))):
                                    for p4 in primes[index3+1:]:
                                        index4 = primes.index(p4)
                                        if miller_rabin(int(str(p1)+str(p4))):
                                            if miller_rabin(int(str(p4)+str(p1))):
                                                if miller_rabin(int(str(p2)+str(p4))):
                                                    if miller_rabin(int(str(p4)+str(p2))):
                                                        if miller_rabin(int(str(p3)+str(p4))):
                                                            if miller_rabin(int(str(p4)+str(p3))):
                                                                for p5 in primes[index4+1:]:
                                                                    index5 = primes.index(p5)
                                                                    if miller_rabin(int(str(p4)+str(p5))):
                                                                        if miller_rabin(int(str(p5)+str(p4))):
                                                                            if miller_rabin(int(str(p2)+str(p5))):
                                                                                if miller_rabin(int(str(p5)+str(p2))):
                                                                                    if miller_rabin(int(str(p3)+str(p5))):
                                                                                        if miller_rabin(int(str(p5)+str(p3))):
                                                                                            if miller_rabin(int(str(p1)+str(p5))):
                                                                                                if miller_rabin(int(str(p5)+str(p1))):
                                                                                                    print(p1, p2, p3, p4, p5)
                                                                                                    print(p1+p2+p3+p4+p5)
                                                                                                    end_time = time.time()
                                                                                                    print(end_time - start_time)
                                                                                                    break

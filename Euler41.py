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

#create pandigitals
panprime = []

# Python program to print all permutations using
# Heap's algorithm

# Prints the array
def printArr(a, n):
    for i in range(n):
        print(a[i], end=" ")
    print()


# Generating permutation using Heap Algorithm
def heapPermutation(a, size, n):
    # if size becomes 1 then prints the obtained
    # permutation
    if (size == 1 ):
        printArr(a, n)
        b = ""
        for i in a:
            b = b + str(i)
        b = int(b)
        z = 0
        x = 0
        for i in primes:
            if i < b:
                z = b % i
                if z == 0:
                    x = x + 1
        if x == 0:
            panprime.append(b)
        panprime.sort()
        print (panprime)


    for i in range(size):
        heapPermutation(a, size - 1, n)

        # if size is odd, swap first and last
        # element
        # else If size is even, swap ith and last element
        if size & 1:
            a[0], a[size - 1] = a[size - 1], a[0]
        else:
            a[i], a[size - 1] = a[size - 1], a[i]

        # Driver code


a = [1, 2, 3, 4, 5, 6, 7]
n = len(a)
heapPermutation(a, n, n)

# This code is contributed by ankush_953
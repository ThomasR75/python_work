#Goldbachs other conjecture
import math
#create list of primes
primemax = 100000
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
print (primes)

#create odd number and check if conjecture holds
end = 9999
start = 9
possible = []
while start < end:
    if start in primes:
        start += 2
    else:
        possible.append(start)
        start += 2
length = len(possible)
bre = 0
for i in possible:
    x = 0
    residual = []
    while i > primes[x]:
        residual.append(i - primes[x])
        x += 1
    #print(residual)
    square = []
    for j in residual:
        if math.sqrt(j/2).is_integer():
            square.append(j)
    #print(square)
    if len(square) == 0:
        print(i)
#print(possible)

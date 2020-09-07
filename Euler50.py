#Euler50 consecutive prime sum
#largest prime below 1mio made up of sequentiel primes


#list of primes
from time import time
begin = time()
primemax = 1000000
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

primemax1 = 4000
marked1 = [0] * primemax1
primes1 = [2, ]
value1 = 3

while value1 < primemax1:
    if marked1[value1] == 0:
        primes1.append(value1)
        i = value1
        while i < primemax1:
            marked1[i] = 1
            i += value1
    value1 += 2
print (primes1)

sum = 0
index1 = 0
index2 = 0
results = []
count = len(primes1)
while index1 < count:
    sum = 0
    while index2 < count - index1:
        sum += primes1[index2]
        index2 += 1
        if sum in primes and index2-index1 > 10:
            results.append(sum)
            results.append(index2-index1)
            #print(index2)
    index1 += 1
    index2 = index1

#print (results)
#print (max(results))
length = len(results)
items = []
x = 1
while x < length:
    items.append(results[x])
    x += 2
#print (items)
#print (max(items))
place = items.index(max(items))
#print (place)
print (results[place*2])
end = time()
print("Time: ", end-begin)

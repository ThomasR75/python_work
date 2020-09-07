#Euler51 Prime Digit replacements
# replace 2 digits in a number with same numbers and find smallest that is 8 number sequence prime

#create primes
from time import time
from collections import Counter
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
#reduce primes to primes with triplicates

primes = [x for x in primes if len(str(x)) - len(set(str(x))) >= 3]

print(len(primes))
checked =[]

#defination to swap duplicates and make list of all
def pdr(s):
    s = str(s)
    sol = []
    for duplicate in (Counter(s) - Counter(set(s)) ):
        a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        temp = [int(s.replace(duplicate, x)) for x in a]
        sol.append(temp)
    return sol

#definition to check if prime numbers
def check(l):
    for i in l:
        checked.append(i)
        if i not in primes:
            l.remove(i)
    return l

flag = True

i = 0

while flag:
    if primes[i] not in checked:
        replacements = pdr(primes[i])
        for j in replacements:
            if len(check(j)) == 8:
                print(j[0])
                flag = False
                break
    i += 1



end = time()
print ("Time: ", end - begin)
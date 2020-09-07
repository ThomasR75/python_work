#Euler51 Prime Digit replacements
# replace 2 digits in a number with same numbers and find smallest that is 8 number sequence prime

#create primes
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
#print (primes)
total = []
number = []
counter = 0
text = ''
for i in range(56001, 56999, 2):
    i = str(i)
    for j in i:
        number.append(j)
    digits = len(number)
    for a in range (0, 10):
        number[digits-2] = str(a)
        number[digits-3] = str(a)
        for i in number:
            text += i
            numbers = int(text)

        #if numbers in primes:
            counter += 1
        #if counter == 7:
        #    print (numbers)

        #print (numbers)
        total.append(numbers)
        text = ''
    number = []
    counter = 0
    text = ''
print(total)
print(len(total))
f = 0
for i in total:
    f += 1
    if i in primes:
        counter += 1
    if counter == 7:
        print (i)
    if f % 10 == 0:
        counter = 0
    #print (i)
    #print (counter)
    #print (f)
end = time()
print("Time: ", end - begin)

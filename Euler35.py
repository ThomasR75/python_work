# Euler 35 Number of Circular Primes < 1mio.
# Create Primes below 1mio
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

# Test if all rotations are primes
a = len(primes)
#print(a)
item = 0
circularlist = []
while item < a:
    z = 0
    x = 0
    number = primes[item]
    numberstr = str(number)
    numbercounter = len(numberstr)
    rotationlist = []
    while z < numbercounter:
        if int(numberstr) in primes:
            rotationlist.append(numberstr)
        numberstr = str(numberstr[1:] + numberstr[0])
        z += 1
    if len(rotationlist) == numbercounter:
        for j in rotationlist:
            if j not in circularlist:
                circularlist.append(j)
    item += 1
print(circularlist)
print(len(circularlist))
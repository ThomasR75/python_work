# Euler 35 Number of Circular Primes < 1mio.
# Create Primes below 1mio
primemax = 102
marked = [0] * primemax
primes = [2, ]
value = 3
s = 2
while value < primemax:
    if marked[value] == 0:
        primes.append(value)
        i = value
        while i < primemax:
            marked[i] = 1
            i += value
    value += 2
print (primes)

# Test if all rotations are primes
a = len(primes)
print(a)
item = 0
circularlist = []
while item < a:
    stumble = 0
    z = 0
    x = 0
    number = primes[item]
    numberstring = str(number)
    newnumberstring = str(number)
    numbercounter = len(newnumberstring)
    while z < numbercounter:
        numberstring1 = newnumberstring[0:1]
        numberstring2 = newnumberstring[1:]
        newnumberstring = numberstring2+numberstring1
        print(numbercounter)
        if int(newnumberstring) not in primes:
            stumble += 1
            print (stumble)
        z += 1
        if stumble < 1:
            newnewnumberstring = str(number)
            newnumbercounter = len(newnewnumberstring)
            while x < newnumbercounter:
                numberstring1 = newnewnumberstring[0:1]
                numberstring2 = newnewnumberstring[1:]
                if int(newnewnumberstring) not in circularlist:
                    circularlist.append(int(newnewnumberstring))
                    print (stumble)
                newnewnumberstring = numberstring2 + numberstring1

                x += 1

    item += 1
print(circularlist)
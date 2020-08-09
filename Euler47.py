#Euler47
#consecutive numbers with same digit prime factors
start1 = 99999
div = 2
step = 0
#find prime factors
factors = []
integers = []
while start1 < 299999:
    start = start1
    while div < start1:
        step = start / div
        if step.is_integer():
            factors.append(div)
            start = step
        else:
            div += 1
    factorset = set(factors)
    if len (list (factorset)) == 4:
        integers.append(start1)

    div = 2
    start1 += 1
    factors = []
count = len(integers)
x = 0
while x < count:
    if integers[x] * 3 == integers[x+1] + integers[x+2] + integers[x+3] - 6:
            #if integers[x] == integers[x+3] - 3:
                print (integers[x])
                x += 1
    else:
        x += 1

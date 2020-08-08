#Euler47
#consecutive numbers with same digit prime factors

start = 10
div = 2
step = 0
#find prime factors
factors = []
while div < math.sqrt(start):
    step = start / div
    if step.is_integer():
        factors.append(div)

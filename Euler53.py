#Euler53 combinatoric selection
from time import time
import math
start = time()
numbers = []
i = 1
j = 1
while i < 101:
    while j < i:
        x = math.factorial(i) / (math.factorial(j) * math.factorial(i-j))
        if x > 1000000:
            numbers.append(x)
        j += 1
    j = 1
    i += 1
print (len(numbers))
end = time()
print ("Time: ", end- start)
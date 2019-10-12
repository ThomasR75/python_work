# Euler 30
# find the sum of all numbers whose digits to the fifth power add to the number

power = 5
start = 11
z = 0
numbers = []
g = 0
while start < 1000000:
    for d in str(start):
        x = int(d)**power
        z = z + x
    if z == start:
        numbers.append(z)
        g = g + z
    z = 0
    start += 1
print(numbers)
print(g)

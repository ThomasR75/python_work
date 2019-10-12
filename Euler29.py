# Euler 29
# How many distinct numbers in integer combinations for a^b for 2<=a<=100 and 2<=b<=100?

a = 2
b = 2
terms = []
while a < 101:
    while b < 101:
        c = a**b
        if c not in terms:
            terms.append(c)
        b += 1
    b = 2
    a += 1
# print(terms)
z = len(terms)
print(z)
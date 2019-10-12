#first fibonacci number with 1000 digits

a = 1
b = 2
c = a + b
v = len(str(a))
i = 3
while v < 1000:
    c = a + b
    v = len(str(c))
    a = b
    b = c
    i += 1
#print(c)
print(i)

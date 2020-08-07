#Euler 48
#find last ten digits of self powered series

x = 1
z = 0
while x < 1001:
    z += x**x
    x += 1
print(z)

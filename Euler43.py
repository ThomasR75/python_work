#Euler43 pandigital substring divisibilty

def heapPermutation(a, size, n):

    for i in range(size):
        heapPermutation(a, size - 1, n)

        # if size is odd, swap first and last
        # element
        # else If size is even, swap ith and last element
        if size & 1:
            a[0], a[size - 1] = a[size - 1], a[0]
        else:
            a[i], a[size - 1] = a[size - 1], a[i]

        # Driver code
    if size == 1:
        for i in range(n):
            #print(a[i], end=" ")
            pandigits.append(a[i])
        #print()

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(a)
pandigits = []
heapPermutation(a, n, n)
print(pandigits)
count = len(pandigits)
x = 1

numbers = []
print (count)
while x < count:
    string = ""
    i = 1
    while i <= n:
        string = string + str (pandigits[i+x-2])
        i += 1
    numbers.append(string)
    x += n
print (numbers)
print(len(numbers))
div2 = []
counter = 0
for j in numbers:
    z = int(j[1:4]) % 2
    #print(int(j[1:4]))
    counter += 1
    if z == 0:
        div2.append(j)
#print (div2)
#print (counter)
#print (len(div2))
div3 = []
counter = 0
for j in div2:
    z = int(j[2:5]) % 3
    #print(int(j[1:4]))
    counter += 1
    if z == 0:
        div3.append(j)
print (div3)
print (counter)
print (len(div3))
div5 = []
counter = 0
for j in div3:
    z = int(j[3:6]) % 5
    #print(int(j[1:4]))
    counter += 1
    if z == 0:
        div5.append(j)
print (div5)
print (counter)
print (len(div5))
div7 = []
counter = 0
for j in div5:
    z = int(j[4:7]) % 7
    #print(int(j[1:4]))
    counter += 1
    if z == 0:
        div7.append(j)
print (div7)
print (counter)
print (len(div7))
div11 = []
counter = 0
for j in div7:
    z = int(j[5:8]) % 11
    #print(int(j[1:4]))
    counter += 1
    if z == 0:
        div11.append(j)
print (div11)
print (counter)
print (len(div11))
div13 = []
counter = 0
for j in div11:
    z = int(j[6:9]) % 13
    #print(int(j[1:4]))
    counter += 1
    if z == 0:
        div13.append(j)
print (div13)
print (counter)
print (len(div13))
div17 = []
counter = 0
for j in div13:
    z = int(j[7:10]) % 17
    #print(int(j[1:4]))
    counter += 1
    if z == 0:
        div17.append(j)
print (div17)
print (counter)
print (len(div17))
sumofall = 0
for j in div17:
    sumofall = sumofall + int(j)
print (sumofall)
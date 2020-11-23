#Euler 55 Lychrel Numbers

from time import time
start = time()

Lychrels =[]
counter = 0
numbers = 12
number = 0

while numbers < 10000:
    counter = 0
    number = numbers
    while counter < 50:
        revnumber = int(str(number)[::-1])
        number = number + revnumber
        if number == int(str(number)[::-1]):
            break
        if counter == 49:
            Lychrels.append(numbers)
        #print (revnumber)
        counter += 1
    numbers += 1
print (len(Lychrels))

end = time()
print ("Time:", end -  start)


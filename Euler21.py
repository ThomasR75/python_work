#Euler 21 Amicable numbers
number = 6
div = 2
list1 = [1]
sumlist1 = 0
sumlist2 = 0
totallist = []
sumtotal = 0
while number < 10000:

#create divisor list for given number
    print(number)
    while div < number:
        if number % div == 0:
            list1.append(number / div)
        div = div + 1
    print(list1)
    #sum the list
    for i in list1:
        sumlist1 += i

    #set div back to 2 and empty list1
    div = 2
    list1 = [1]

    #test sum of list 1 for divisors
    while div < sumlist1:
        if sumlist1 % div == 0:
            list1.append(sumlist1 / div)
        div = div + 1
    print(list1)
    div = 2
    #sum the new list to sumlist2
    for i in list1:
        sumlist2 += i
    #check if sumlist2 is equal to original number
    if sumlist2 == number and sumlist1 != sumlist2:
        totallist.append(number)
        totallist.append(sumlist1)

    print(sumlist1)
    print(sumlist2)
    sumlist1 = 0
    sumlist2 = 0
    list1 = [1]
    number += 1

print(totallist)
for i in totallist:
    sumtotal += i
print(sumtotal / 2)
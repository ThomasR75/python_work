#Euler problem 16
	
n = input("2 to the power of:")
number = 2 ** (int(n))
print (number)
text = str(number)
digits = len (text)
listtext = []
listtext = [int(d) for d in text]
a = 0
summe = 0
print(listtext)
while a < digits:
	summe = summe + listtext[a]
	a = a + 1
print (digits)
print (summe)


#largest collatz sequence under 1mio

def collatz(number):
	
    if number % 2 == 0:
        #print(number // 2)
        numbers.append(number // 2)
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        #print(result)
        numbers.append(result)
        return result
counter = 1000000
digits = []
while counter > 499999:
	numbers = []
	#n = input("Give me a number: ")
	n = counter
	while n != 1:
		n = collatz(int(n))
	
	#print(numbers)
	#digits = len(numbers)
	digits.append(len(numbers))
	counter = counter - 1
large = max(digits)
print(large)
place = digits.index(large)
print (place)

#print(digits)

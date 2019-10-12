# Euler Number letter counts
# numbers 1 to 5 in letters are 19, what about 1 to 1000
import num2words
numbers = list(range(1, 1001))
strings = []
connected_string = ""
a = 1
b = len(numbers)

while a <= b:
    z = num2words.num2words(a)
    strings.append(z)
    a = a+1
for i in strings:
    connected_string += str(i)
print(connected_string)
print(len(connected_string))
print(connected_string.count("-"))
print(connected_string.count(" "))
# print(numbers[:])
# print(strings)

#Euler42 triangle words

import string
words = []
words_file = open("p042_words.txt", "r")
words = words_file.read().replace('"', '').split(",")
words_file.close()

alpha = list(string.ascii_uppercase)
print (alpha)
sums = []

for i in words:
    summe = 0
    value = 0
    for l in i:
        value = alpha.index(l) + 1
        summe = summe + value
    sums.append(summe)
maximum = max (sums)
counter = 0
base = list(range(1, maximum+1))
tribase = []
for i in base:
    tribase.append(0.5*i*(i+1))
for i in sums:
    if i in tribase:
        counter += 1
print (counter)

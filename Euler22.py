#Euler22 Namescores
names = []
names_file = open("p022_names.txt", "r")
names = names_file.read().replace('"', '').split(",")
names_file.close()
names.sort()
print(names)
counter = len(names)
print(counter)
listn = 0
item = 0
while item < counter:
    obj = ""
    obj = names[item]
    buchn = 0
    for buch in obj:
        buch = ord(buch) - 64
        buchn = buchn + buch
    #print(buchn)
    item = item + 1
    wordn = item * buchn
    #print(wordn)
    listn = listn + wordn
print(listn)

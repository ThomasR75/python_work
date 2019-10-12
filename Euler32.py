# Euler 32, Pan Digital Products

start1 = 1
start2 = 1
comparison = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list = []
final = []
finalsum = 0
while start1 < 100:
    while start2 < 9999:
        start3 = start1 * start2
        for i in str(start3):
            list.append(int(i))
        for i in str(start2):
            list.append(int(i))
        for i in str(start1):
            list.append(int(i))
        list.sort()
        # print(list)
        if list == comparison and start3 not in final:
            final.append(start3)
            finalsum += start3
        list = []
        start2 += 1
    start2 = 1
    start1 += 1
print(final)
print(finalsum)

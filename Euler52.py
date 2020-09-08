#Euler52 check if multiples are permutations of original number

from time import time

begin = time()

start = 1
while start < 1000000:


    start2 = start * 2
    start3 = start * 3
    start4 = start * 4
    start5 = start * 5
    start6 = start * 6

    startstr1 = sorted(set(str(start)))
    startstr2 = sorted(set(str(start2)))
    startstr3 = sorted(set(str(start3)))
    startstr4 = sorted(set(str(start4)))
    startstr5 = sorted(set(str(start5)))
    startstr6 = sorted(set(str(start6)))
#   print (startstr1)
#    print (startstr2)
    if startstr1 == startstr2:
        if startstr2 == startstr3:
            if startstr4 == startstr3:
                if startstr5 == startstr4:
                    if startstr6 == startstr5:

                        print("Yeah", start)
#    else:
#        print("No")

    start += 1

end = time()
print("Time: ", end - begin)

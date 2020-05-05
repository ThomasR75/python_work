#Euler44 Pentagonal Numbers Smallest difference between sum and difference

#Create first 10,000

PenNum = []
N = list(range(1, 5000))
#print (N)
for i in N:
    PenNum.append(i*(3*i-1)/2)
print (PenNum)
i = 0
PenDiffList = []

while i < len(PenNum):
    steps = 1
    while steps < len(PenNum) - i + 1:
        PenDiff = PenNum[i + steps - 1] - PenNum[i]
        #print (PenDiff, i, steps)
        if PenDiff in PenNum:
            #print (PenDiff)
            PenSum = PenNum[i] + PenNum[i + steps - 1]
            if PenSum in PenNum:
                PenDiffList.append(PenDiff)
        steps += 1
    i = i + 1

print (PenDiffList)


#Euler44 Pentagonal Numbers Smallest difference between sum and difference

#Create first 10,000

PenNum = []
N = list(range(1, 10000))
#print (N)
for i in N:
    PenNum.append(i*(3*i-1)/2)
print (PenNum)
i = 0
PenDiffList = []
PenSumList = []
PenMixedList =[]
while i < len(PenNum):
    steps = 1
    while steps < len(PenNum) - i + 1:
        PenDiff = PenNum[i + steps - 1] - PenNum[i]
        #print (PenDiff, i, steps)
        if PenDiff in PenNum:
            PenDiffList.append (PenDiff)
        steps += 1
    i = i + 1

i = 0
while i < len(PenNum):
    steps = 1
    while steps < len(PenNum) - i + 1:
        PenSum = PenNum[i] + PenNum[i + steps - 1]
        if PenSum in PenNum:
            PenSumList.append(PenSum)
        steps += 1
    i = i + 1
for i in PenSumList:
    if i in PenDiffList:
        PenMixedList.append (i)
PenDiffList.sort()
PenSumList.sort()
PenMixedList.sort()
print (PenSumList)
print (PenDiffList)
print (PenMixedList)


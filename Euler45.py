#Euler45 find number that is triangle, pentagonal and hexagonal > 40755

#Create Number lists
N = 100000
TriNums = []
for i in range (1,N):
    TriNums.append(i * (i + 1)/2)
PenNums = []
for i in range (1,N):
    PenNums.append(i * (3 * i - 1)/2)
HexNums = []
for i in range (1,N):
    HexNums.append(i * (2 * i - 1))

#Check if Num in other list
CombNum = []
for i in TriNums:
    if i in PenNums:
        if i in HexNums:
            CombNum.append(i)
print (CombNum)

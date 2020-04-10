#Euler 38 find largest 9 digit pandigital as multiple of X and (1,2,3...n) concatenated
# X has to be 4 digit number as 2 and 3digit numbers generate only 7, 8 or 11 digit result if multiplied n=3 or 4
start = 9234
end = 9999
result = 0;
palindrome = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test = []
list = []
sample = 918273645
while start < end:
    result = 2 * start
    test = int(str(start)+str(result))
    for i in str(test):
        list.append(int(i))
        list.sort()
        if list == palindrome and test > sample:
            sample = test
    list = []
    start += 1
print(sample)

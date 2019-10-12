nums = '\
08 06 78 56 96\n\
45 63 68 23 51\n\
63 78 45 08 37\n\
56 73 92 73 83\n\
43 22 67 98 55'
grid = []
for line in nums.split('\n'):
    grid.append(list(map(int, line.split())))
print (grid)


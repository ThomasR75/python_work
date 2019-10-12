# Euler Problem 18
# maximum sum of paths
import numpy as np
text_file = open("p067_triangle.txt", "r")
lines = text_file.read()
text_file.close()
#print(lines)
grid = []
for line in lines.split(','):
    grid.append(list(map(int, line.split())))
# print(grid)
numbs1 = grid[0]
# print(numbs1)
numbs = numbs1
data1 = np.zeros((100, 100))
a = 0
b = 0
c = 0
z = 1
while b < 100:
    while a < b + z:
        data1[b, c] = data1[b, c] + numbs[a]
        a = a + 1
        c = c + 1
    b = b + 1
    z = z + b
    c = 0
print(data1)
m = 99
n = 99
while m > 0:
    while n > 0:
        data1[m-1, n-1] = data1[m-1, n-1] + max(data1[m, n-1], data1[m, n])
        n = n - 1
    m = m - 1
    n = 99
print(data1)

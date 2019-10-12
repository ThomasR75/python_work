# Euler28 spiral grid
start = 1
step = 2
counter = 1
sum = 1
loop = 1
while loop < 501:
    while counter < 5:
        start = start + step
        sum = sum + start
        counter += 1
    step += 2
    loop += 1
    counter = 1
print(sum)


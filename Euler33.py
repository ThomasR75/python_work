# Euler 33, Digit cancelling fractions

denom_start = 99
num_start = 98
denom_string = []
num_string = []
result_string = []
while denom_start > 12:
    while num_start > 11:
        for i in str(denom_start):
            denom_string.append(int(i))
        for i in str(num_start):
            num_string.append(int(i))
        if num_string[0] == denom_string[0]:
            if num_string[1]/denom_string[1] == num_start/denom_start and num_start/denom_start < 1:
                result_string.append(num_start)
                result_string.append(denom_start)
        if num_string[0] == denom_string[1]:
            if num_string[1] / denom_string[0] == num_start / denom_start and num_start / denom_start < 1:
                result_string.append(num_start)
                result_string.append(denom_start)
        if num_string[1] == denom_string[0]:
            if num_string[0] / denom_string[1] == num_start / denom_start and num_start / denom_start < 1:
                result_string.append(num_start)
                result_string.append(denom_start)
        if num_string[1] == denom_string[1]:
            if num_string[0] / denom_string[0] == num_start / denom_start and num_start / denom_start < 1:
                result_string.append(num_start)
                result_string.append(denom_start)
        print(num_string)
        print(denom_string)
        num_string = []
        denom_string = []
        num_start = num_start - 1


    num_start = 98

    denom_start = denom_start - 1
    if denom_start % 10 == 0:
        denom_start = denom_start - 1

print(result_string)

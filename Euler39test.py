p_list = [0 for i in range(1001)]
for a in range(1,1000):
    for b in range(1,1000):
        c = (a**2 + b**2)**0.5
        if c == int(c) and c+a+b <= 1000:
            c = int(c)
            p_list[a+b+c] += 1

print(p_list.index(max(p_list)))
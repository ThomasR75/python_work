def digital_root(n):
    # ...
    x = 0
    if len(str(n))>1:
        x = x + [int(n) for n in str(n)]
        return (x)

digital_root(22)


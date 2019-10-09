def persistence(n):
    if n < 10:
        return 0

    i = 0
    r = 0
    while n > 9:
        lstn = list(str(n))
        n = 1
        for i in lstn:
            n = n * int(i)
        r += 1
    return r

def next_bigger(n):
    string = str(n)
    ps = set()  # ps to hold all permutations of s
    ps.add(string[0])
    l = len(string)
    i = 1
    while i < l:
        tmp_ps = set()
        for p in ps:
            ll = len(p)
            ii = 0
            while ii <= ll:
                tmp_ps.add(p[:ii]+string[i]+p[ii:])
                ii += 1
        ps = tmp_ps
        i += 1

    ps = list(sorted(ps))

    for x in ps:
        if int(x) > n:
            return int(x)
    return -1


print(next_bigger(12))  # 21)
print(next_bigger(513))  # 531)
print(next_bigger(2017))  # 2071)
print(next_bigger(414))  # 441)
print(next_bigger(144))  # 414)

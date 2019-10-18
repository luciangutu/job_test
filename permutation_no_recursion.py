def permutations(string):
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
    return ps


print(sorted(permutations('aabb')))  # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
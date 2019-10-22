import itertools


def next_bigger(n):
    if not isinstance(n, int):
        return -1
    result = []
    perm = list(itertools.permutations(str(n)))
    for i in range(len(perm)):
        curr = int(''.join(perm[i]))
        if curr > n:
            result.append(curr)
    try:
        return min(result)
    except:
        return -1


print(next_bigger(12))  # 21)
print(next_bigger(513))  # 531)
print(next_bigger(2017))  # 2071)
print(next_bigger(414))  # 441)
print(next_bigger(144))  # 414)

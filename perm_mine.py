def perm(lst):
    if len(lst) == 1:
        return [lst]
    if len(lst) == 0:
        return []
    result = []
    for i in range(len(lst)):
        keep = lst[i]
        rest = lst[:i] + lst[i+1:]
        for j in perm(rest):
            result.append([keep] + j)
    return result


print(perm([1, 2, 3, 4, 5]))

data = [1, 2, 3]
for p in perm(data):
    print(p)

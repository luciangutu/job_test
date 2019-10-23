# Python function to print permutations of a given list
def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]

    result = []

    for i in range(len(lst)):
        m = lst[i]
        remlst = lst[:i] + lst[i+1:]
        for j in permutation(remlst):
            result.append([m] + j)
    return result


data = [1, 2, 3]
for p in permutation(data):
    print(p)

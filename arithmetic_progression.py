def find_missing(sequence):
    ap = ((len(sequence) + 1) * (sequence[0] + sequence[-1])) / 2
    missing = ap - sum(sequence)
    return int(missing)


print(find_missing([1, 2, 3, 4, 6, 7, 8, 9]))  # 5)
print(find_missing([1, 3, 4, 5, 6, 7, 8, 9]))  # 2)
print(find_missing([1, 3, 5, 9, 11]))
print(find_missing([1, 19, 28, 37, 46]))

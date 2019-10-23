# below functions is using a generator - yield
def permute(sequence, index=0):
    length = len(sequence)

    if index > length:
        raise StopIteration

    if index == length:
        yield sequence
    else:
        for i in range(index, length):
            sequence[i], sequence[index] = sequence[index], sequence[i]
            for permutation in permute(sequence, index + 1):
                yield permutation
            sequence[index], sequence[i] = sequence[i], sequence[index]


for each_permutation in permute([1, 2, 3]):
    print(each_permutation)

# or like this since it's a generator - yield
print("again...")
lst = permute([1, 2, 3])
print(next(lst))
print(next(lst))
print(next(lst))

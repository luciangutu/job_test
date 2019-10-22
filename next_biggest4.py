def next_bigger(n):
    # next-lexicographical-permutation-algorithm
    if n < 9:
        return -1
    arr = list(str(n))
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1

    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # Reverse suffix
    arr[i:] = arr[len(arr) - 1: i - 1: -1]
    return int(''.join(arr))


print(next_bigger(12))  # 21)
print(next_bigger(513))  # 531)
print(next_bigger(2017))  # 2071)
print(next_bigger(414))  # 441)
print(next_bigger(144))  # 414)
print(next_bigger(53365025817051))
print(next_bigger(62815445463543))
print(next_bigger(4152266529565))
print(next_bigger(7962873017505))
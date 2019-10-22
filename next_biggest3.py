def next_bigger(num):
    digits = [int(i) for i in str(num)]
    idx = len(digits) - 1
    while idx >= 1 and digits[idx-1] >= digits[idx]:
        idx -= 1
    if idx == 0:
        return -1
    pivot = digits[idx-1]
    swap_idx = len(digits) - 1
    while pivot >= digits[swap_idx]:
        swap_idx -= 1
    digits[swap_idx], digits[idx-1] = digits[idx-1], digits[swap_idx]
    digits[idx:] = digits[:idx-1:-1]
    return int(''.join(str(x) for x in digits))
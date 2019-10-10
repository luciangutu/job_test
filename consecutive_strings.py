def longest_consec(strarr, k):
    if k == 1:
        return max(strarr, key=len)
    if k < 1:
        return str()
    if k > len(strarr):
        return str()
    prev_word = str()
    for n in range(0, len(strarr)):
        curr_word = ''.join(strarr[n:n + k])
        if len(curr_word) > len(prev_word):
            prev_word = curr_word
    return prev_word


print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))  # "abigailtheta"
print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3))  # "ixoyx3452zzzzzzzzzzzz"
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))  # "oocccffuucccjjjkkkjyyyeehh")
print(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 0))  # "")

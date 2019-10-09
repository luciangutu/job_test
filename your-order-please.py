def order(sentence):
    mylist = sentence.split()
    result_dict = {}
    for words in mylist:
        for char in words:
            if char.isdigit():
                result_dict[int(char)] = words
    #return result_dict.items()
    return ' '.join([value for (key, value) in sorted(result_dict.items())])

print(order("3 4 2 6 7 5 1 8 9"))
print(order("is2 Thi1s T4est 3a"))

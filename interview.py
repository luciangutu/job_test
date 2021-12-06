my_list = [1, 3, 2, 1, 4, 3, 1, 0, 1, 3]
for p in my_list:
    pass
    if (p == 0):
       curr = p
       break
    elif (p % 2 == 0):
       continue
    print(p)
print(curr)

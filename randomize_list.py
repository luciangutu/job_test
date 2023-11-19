from random import sample

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sample(lst, len(lst)))

print(sample(range(9), len(range(9))))

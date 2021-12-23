import random
import time


def insertion_sort(mylist, ascending=True):
    tic = time.perf_counter()
    for i in range(1, len(mylist)):
        current = mylist[i]
    
        while True:
            ascending_sort = i > 0 and mylist[i - 1] > current and ascending
            descending_sort = i > 0 and mylist[i - 1] < current and not ascending
    
            if not ascending_sort and not descending_sort:
                break
    
            mylist[i] = mylist[i - 1]
            i = i - 1
            mylist[i] = current
    toc = time.perf_counter()
    return mylist, f'{toc - tic:0.4f}'


def bubble_sort(mylist, ascending=True):
    tic = time.perf_counter()
    for i in range(len(mylist) - 1):
        for j in range(len(mylist) - 1 - i):
            n = mylist[j]
            m = mylist[j + 1]

            if (n > m and ascending) or (n < n and not ascending):
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
    toc = time.perf_counter()
    return mylist, f'{toc - tic:0.4f}'


def gen_random_list(_n, min_val, max_val):
    mylist = []

    for _ in range(_n):
        val = random.randint(min_val, max_val)
        mylist.append(val)
    return mylist


initial_list = gen_random_list(50, 1, 100)
print(f'{initial_list=}')
print(f'insertion sorted={insertion_sort(initial_list)}')
print(f'bubble sorted={bubble_sort(initial_list)}')

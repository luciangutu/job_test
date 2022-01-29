#!/usr/bin/python
# https://www.hackerrank.com/challenges/nested-list/problem

records = [["ccc", 10], ["bbb", 20], ["ddd", 20], ["ggg", 70], ["fff", 50]]

# records = [['Sona', -25.001], ['Mona', -25.0001], ['Mini', -25.000],
#            ['Rita', -25.000]]

records = sorted(records)

def num_sort(_mylist):
    for i in range(0, len(_mylist)):
        for j in range(0, len(_mylist) - i - 1):
            if _mylist[j][1] > _mylist[j + 1][1]:
                tempo = _mylist[j]
                _mylist[j] = _mylist[j + 1]
                _mylist[j + 1] = tempo
    return _mylist


def remove_elem(_mylist, _min):
    return [num for num in _mylist if num[1] != _min ]


def keep_only(_mylist, _elem_to_keep):
    return [num for num in _mylist if num[1] == _elem_to_keep ]


records = num_sort(records)
min_elem = records[0][1]

records = remove_elem(records, min_elem)
keep_elem = records[0][1]
results = keep_only(records, keep_elem)
if results:
    for result in results:
        print(result[0])
else:
    exit


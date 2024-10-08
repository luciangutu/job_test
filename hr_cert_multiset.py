#!/bin/python
# HackerRank certification
import math
import os
import random
import re
import sys


class Multiset(object):
    def __init__(self, val=None):
        self.val = val
        self.val_list = []
    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        self.val_list.append(val)

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        if self.__contains__(val):
            self.val_list.remove(val)
        return self

    def show(self):
        return self.val_list

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        if val in self.val_list:
            return True
        return False

    def __len__(self):
        # returns the number of elements in the multiset
        return len(self.val_list)


if __name__ == '__main__':
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            elif elems[0] == 'show':
                print(m.show())
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)

        return result


    q = int(input())
    operations = []
    for _ in range(q):
        operations.append(input())

    result = performOperations(operations)

    print('\n'.join(map(str, result)))
    print('\n')

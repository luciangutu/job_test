#!/bin/python
import math
import os
import random
import re
import sys


# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    # check the limits
    if (1 > len(s) > 100) or (1 > len(t) > 100) or (1 > k > 100):
        return "No"
    # check for lowercase
    if not any(c.islower() for c in s):
        return "No"
    if not any(c.islower() for c in t):
        return "No"
    # check if the strings are equal
    # if s == t and len(s)+len(t) <= k:
    if s == t and k % 2 == 0:
        return "Yes"

    s = list(s)
    t = list(t)
    counter = 0

    for i in range(len(t)):
        if i > len(s)-1:
            break
        if s[i] == t[i]:
            counter += 1
            continue
        else:
            break
    # check if the sum of the remaining chars is less than the number of remaining operations
    if (len(s) - counter) + (len(t) - counter) > k:
        return "No"
    # check if the sum of the remaining chars is equal to k or k is even number
    # if (len(s)-counter) + (len(t)-counter) == k:
    if ((len(s) - counter) + (len(t) - counter) - k) % 2 == 0:
        return "Yes"
    # check if we have more operations than characters in both strings
    if len(s) + len(t) - k < 0:
        return "Yes"
    return "No"


s = 'hackerhappy'
t = 'hackerrank'
k = 9
result = appendAndDelete(s, t, k)
print(result)

s = 'aba'
t = 'aba'
k = 7
result = appendAndDelete(s, t, k)
print(result)

s = 'ashley'
t = 'ash'
k = 2
result = appendAndDelete(s, t, k)
print(result)

s = 'a'
t = 'abc'
k = 5
result = appendAndDelete(s, t, k)
print(result)

s = 'a'
t = 'abc'
k = 4
result = appendAndDelete(s, t, k)
print(result)


s = 'qwerty'
t = 'qwerui'
k = 2
result = appendAndDelete(s, t, k)
print(result)
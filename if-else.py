#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if 1 < n > 100:
        exit(1)
    if n % 2 != 0:
        print("Weird")
        exit(0)
    if n % 2 == 0:
        if 2 <= n <= 5 or n > 20:
            print("Not Weird")
            exit(0)
        if 6 <= n <= 20:
            print("Weird")
            exit(0)

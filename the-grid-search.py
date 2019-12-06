#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the gridSearch function below.
def gridSearch(G, P):
    # print(r, R, c, C)
    if 0 > t > 6 or 0 > R > 1001 or 0 > r > 1001 or 0 > C > 1001 or 0 > c > 1001:
        return "NO"
    if 0 > r > R:
        return "NO"
    if 0 > c > C:
        return "NO"

    # got_one = 0
    # for i in G:
    #     for j in P:
    #         # print(i, j, got_one, r)
    #         if got_one >= r:
    #             return "YES"
    #         if str(i).find(str(j)) > 0:
    #             got_one += 1
    #             P.remove(j)
    #             break
    #         else:
    #             got_one = 0
    # if got_one == r:
    #     return "YES"
    # else:
    #     return "NO"

    got_one = 0
    for i in range(len(G)):
        for j in range(len(P)):
            # print(G[i], P[j], got_one, r)
            # we reached the end of the pattern and we got all of the elements
            if got_one >= r:
                return "YES"
            # search the pattern
            if str(G[i]).find(str(P[j])) > 0:
                got_one += 1
                del P[j]
                break
            else:
                got_one = 0
                # if the 1st element from the 2nd array (pattern) is not found,
                # then there is no point on checking the rest of them
                if j == 0:
                    break
    if got_one == r:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        RC = input().split()
        R = int(RC[0])
        C = int(RC[1])
        G = []
        for _ in range(R):
            G_item = input()
            G.append(G_item)
        rc = input().split()
        r = int(rc[0])
        c = int(rc[1])
        P = []
        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)
        print(result + '\n')


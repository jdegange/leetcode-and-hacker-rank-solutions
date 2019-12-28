#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_locs = []
    orange_locs = []
    apple_in_house = []
    orange_in_house = []
    for i in apples:
        apple_locs.append(a+i)
    for j in oranges:
        orange_locs.append(b+j)
    for k in apple_locs:
        if k in range(s,t+1):
            apple_in_house.append(k)
    for l in orange_locs:
        if l in range(s,t+1):
            orange_in_house.append(l)
    
    print(len(apple_in_house))
    print(len(orange_in_house))


    

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

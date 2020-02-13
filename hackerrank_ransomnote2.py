#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    dict = {}
    for i in magazine:
        if i in dict:
            dict[i] = dict[i]+1
        else:
            dict[i] = 1
    verdict = "Yes"
    for j in note:
        if j in dict and dict[j] >=1:
            dict[j] -=1
        else:
            verdict = "No"
            break
    print(verdict)
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

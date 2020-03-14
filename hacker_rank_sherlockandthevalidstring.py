#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    #1 get the dictionary
    dict = {}
    #if not in, initialize with 0, else add 1
    for i in s:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    changes = 0
    verdict = "YES"
    #allow one change only
    for j in dict:
        if dict[j] %2 != 0 and changes <1 :
            if dict[j] >1:
                dict[j] -= 1
            else:
                del dict[j]
            break
            changes +=1
    #if not all the same return no
    for k in dict:
        if any(value != dict[k] for value in dict.values()):
            return "NO"

    #If count isn't even ret no
    for k in dict:
        if dict[k] %2 != 0:
            return "NO"

    return verdict
    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    a_sort = sorted(a)
    b_sort = sorted(b)
    count = 0
    cands = []
    for i in list(range(a_sort[-1],b_sort[0]+1,1)):
        a_count = 0
        for j in a_sort:
            if i%j == 0:
                a_count +=1
        if a_count == len(a_sort):
            cands.append(i)
    for k in cands:
        b_count = 0
        for l in b_sort:
            if l%k == 0:
                b_count +=1
        if b_count == len(b_sort):
            print(k)
            count +=1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()

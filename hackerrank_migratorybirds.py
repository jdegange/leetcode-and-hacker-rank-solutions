#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    arr = sorted(arr)
    print(arr)
    dict = {}
    for i in arr:
        if i in dict:
            dict[i] +=1
        else:
            dict[i] = 1
    return max(dict,key=dict.get)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

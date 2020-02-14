#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    cur_pos = 0
    last_pos = len(c)-1
    while cur_pos < last_pos:
        if last_pos - cur_pos >=2 and c[cur_pos +2] != 1:
            cur_pos +=2
        else:
            cur_pos +=1
        jumps += 1
        print(len(c),cur_pos,jumps)
    return jumps
    




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

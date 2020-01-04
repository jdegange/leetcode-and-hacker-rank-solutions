#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    high_score_count = low_score_count = high_score = low_score = 0
    for count,i in enumerate(scores):
        if count == 0:
            high_score = low_score = i
        if i > high_score:
            high_score = i
            high_score_count += 1
        if i < low_score:
            low_score = i
            low_score_count += 1
        print(i, low_score, high_score)
    return high_score_count,low_score_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

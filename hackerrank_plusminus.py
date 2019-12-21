#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.


def plusMinus(arr):
    pos_ = neg_ = zero_ = 0
    for count, i in enumerate(arr):
        if i > 0:
            pos_ += 1
        if i == 0:
            zero_ += 1
        if i < 0:
            neg_ += 1
    count = count +1
    print(f'{pos_/count:.6f}')
    print(f'{neg_/count:.6f}')
    print(f'{zero_/count:.6f}')
 


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

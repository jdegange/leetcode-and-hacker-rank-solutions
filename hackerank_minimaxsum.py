#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr_sort = sorted(list(arr))

    #print(list(arr).sort())
    print(sum(arr_sort[0:4]),sum(arr_sort[1:5]))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

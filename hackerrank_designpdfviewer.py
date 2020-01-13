#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    alfa = "abcdefghijklmnopqrstuvwxyz"
    d = {}
    for i in range(len(h)):
        d[alfa[i]] = h[i]
    max_len = max(d[j] for j in word)
    print(max_len)
    return len(word) * max_len



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()

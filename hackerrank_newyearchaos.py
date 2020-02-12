#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(Q):
    #
    # initialize the number of moves
    moves = 0 
    Q = [P-1 for P in Q]
    #print(Q)
    #
    # Loop through each person (P) in the queue (Q)
    for i,P in enumerate(Q):
        if P - i > 2:
            print("Too chaotic")
            return

        for j in range(max(P-1,0),i):
            if Q[j] > P:
                moves += 1
    print(moves)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

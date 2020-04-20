#!/bin/python3
import math
import os
import random
import re
import sys
from collections import deque

class RunningMedian(object):
    
    def __init__(self, maxLen):
        self.d = [0] * 201
        self.queue = deque()
        self.maxLen = maxLen
    
    def add(self, v: int) -> None:
        self.queue.append(v)
        self.d[v] += 1
        if len(self.queue) > self.maxLen:
            val = self.queue.popleft()
            self.d[val] -= 1
    
    def median(self) -> int:
        a = int(self.maxLen / 2)
        b = a + 1
        mid1 = None
        mid2 = None
        rs = 0
        
        for idx, v in enumerate(self.d):
            rs += v
            if rs >= a and mid1 is None:
                mid1 = idx
            if rs >= b:
                mid2 = idx
                break
        
        if self.maxLen % 2 == 0:
            return (mid1 + mid2) / 2.0
        else:
            return mid2
            

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    notifications = 0
    r = RunningMedian(d)
    for v in expenditure[:d]:
        r.add(v)
        
    for idx, v in enumerate(expenditure[d:]):
        median = r.median()
        # print(median, expenditure[idx: idx+d])
        if v >= (2*median):
            notifications += 1
        r.add(v)
    
    return notifications



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()


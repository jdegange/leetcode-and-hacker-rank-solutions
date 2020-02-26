#!/bin/python3

import math
import os
import random
import re
import sys


def binarySearch(arr, l, r, x): 
    while l <= r: 
        mid = l + (r - l)//2 
        if arr[mid][1] == x: 
            return mid
        elif arr[mid][1] < x: 
            l = mid + 1
        else: 
            r = mid - 1 
    return -1
def Ignore(li,money):
    l=0
    r=len(li)-1
    while l<=r:
        mid=l+(r-1)//2
        if li[mid][1]>=money:
            return mid
        else:
            l=mid+1
    return -1
def whatFlavors(cost, money):
    a=list(enumerate(cost))
    a.sort(key=lambda x:x[1])
    #this ignores the elements equals to or greater than the money in sorted array
    try:
        ignore=Ignore(a,money)
        if ignore==-1:
            ignore=len(a)-1
    except:
        ignore=len(a)-1
    for i in range(ignore):
        index=binarySearch(a,i+1,ignore,money-a[i][1])
        if index!=-1:
            print(min(a[i][0]+1,a[index][0]+1),max(a[i][0]+1,a[index][0]+1))
            break
    

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr): 
    n = len(arr) 
      
    # Create two arrays and use  
    # as pairs where first array  
    # is element and second array 
    # is position of first element 
    arrpos = [*enumerate(arr)] 
      
    # Sort the array by array element  
    # values to get right position of  
    # every element as the elements  
    # of second array. 
    arrpos.sort(key = lambda it:it[1]) 
      
    # To keep track of visited elements.  
    # Initialize all elements as not  
    # visited or false. 
    vis = {k:False for k in range(n)} 
      
    # Initialize result 
    ans = 0
    for i in range(n): 
          
        # alreadt swapped or  
        # alreadt present at  
        # correct position 
        if vis[i] or arrpos[i][0] == i: 
            continue
              
        # find number of nodes  
        # in this cycle and 
        # add it to ans 
        cycle_size = 0
        j = i 
        while not vis[j]: 
              
            # mark node as visited 
            vis[j] = True
              
            # move to next node 
            j = arrpos[j][0] 
            cycle_size += 1
              
        # update answer by adding 
        # current cycle 
        if cycle_size > 0: 
            ans += (cycle_size - 1) 
    # return answer 
    return ans 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

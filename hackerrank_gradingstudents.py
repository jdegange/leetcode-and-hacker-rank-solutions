#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades, base=5):
    grades_round = []
    for i in grades:
        if i < 38:
            grades_round.append(i)
        else:
            print(base * math.ceil(i/base) - i)
            if base * math.ceil(i/base) - i < 3:
                grades_round.append(base * math.ceil(i/base))
            else:
                grades_round.append(i)
    return grades_round
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades,base=5)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

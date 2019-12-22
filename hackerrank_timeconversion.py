#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hour = ''.join(s[0:2])
    if "PM" in s and int(hour) != 12:
        
        new_hour = int(hour)+12
        s = s.replace(hour,str(new_hour))
        s = s.replace("PM","")
    if "PM" in s and int(hour) == 12:
        s = s.replace("PM","")

    if "AM" in s:
        s = s.replace("AM","")
        if hour == str(12):
            s = s.replace(hour,"00")

    
    return(s)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    cambia = False
    new_s=""
    for i in range(len(s)):
        if s[i] == "P":
            cambia=True
            break
        elif s[i] == "A":
            break
        new_s = new_s + s[i]
    if cambia:
        if True:
            n = new_s[0:2]
            if n=="12":
                n="12"
            else:
                if n == "10" or n == "11":
                    n = str(int(new_s[0:2])+12)
                else:
                    n = str(int(new_s[1])+12)
        temp = n + new_s[2:]
        new_s = temp
    else:
        n = new_s[0:2]
        if n=="12":
            n="00"
        temp = n + new_s[2:]
        new_s = temp
    return new_s
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

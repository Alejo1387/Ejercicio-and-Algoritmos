#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    ziro = 0
    pos = 0
    neg = 0
    for i in range(n):
        if arr[i]==0:
            ziro+=1
        elif arr[i]>0:
            pos+=1
        else:
            neg+=1
    ziro/=n
    pos/=n
    neg/=n
    mensaje = f"{pos:.6f} \n {neg:.6f} \n {ziro:.6f}"
    return mensaje

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = plusMinus(arr)
    
    fptr.write(str(result) + '\n')

    fptr.close()

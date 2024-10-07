#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sum1=0
    sum2=0
    n = len(arr)
    arr.sort()
    for i in range(n):
        if i>=0 and i<(n-1):
            sum1 += arr[i]
        if i>=1 and i<=(len(arr)):
            sum2 += arr[i]
    return f"{sum1} {sum2}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = list(map(int, input().rstrip().split()))

    result = miniMaxSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
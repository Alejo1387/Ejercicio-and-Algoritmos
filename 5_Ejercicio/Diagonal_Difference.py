#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    sum1 = 0
    sum2 = 0
    resul = 0
    for i in range(3):
        for j in range(3):
            # Primera suma
            if i==0 and j==0:
                sum1 += arr[i][j]
            if i==1 and j==1:
                sum1 += arr[i][j]
            if i==2 and j==2:
                sum1 += arr[i][j]
            # Segunda suma
            if i==0 and j==2:
                sum2 += arr[i][j]
            if i==1 and j==1:
                sum2 += arr[i][j]
            if i==2 and j==0:
                sum2 += arr[i][j]
    resul = sum1 - sum2
    return abs(resul)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

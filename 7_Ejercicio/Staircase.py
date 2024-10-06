#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    mensaje1 = ""
    k=0
    i=n-1
    n-=1
    while True:
        while k<n:
            mensaje1=mensaje1+" "
            k+=1
        if k==n:
            while k<=i:
                mensaje1=mensaje1+"#"
                k+=1
        if n>0:
            mensaje1 = f"{mensaje1}\n"
            n-=1
            k=0
        elif n==0:
            break
    return mensaje1
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    n = int(input().strip())

    result = staircase(n)

    fptr.write(str(result) + '\n')

    fptr.close()

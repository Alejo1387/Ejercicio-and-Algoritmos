#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    # Forma 1
    # s = s.title()
    
    # Forma 2
    s += " "
    mesage = ""
    texto = ""
    for i in range(len(s)):
        if s[i] == " ":
            mesage = mesage + texto.capitalize() + " "
            texto = ""
        else:
            texto += s[i]
    return mesage

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
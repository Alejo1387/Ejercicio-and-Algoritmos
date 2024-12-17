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

def gradingStudents(grades):
    # Write your code here
    new_list = []
    for i in range(len(grades)):
        if grades[i] < 38:
            new_list.append(grades[i])
        else:
            n = 0
            for j in range(grades[i]):
                n = 5 * j
                if n > grades[i]:
                    break
            results = n - grades[i]
            if results <= 2:
                new_list.append(n)
            else:
                new_list.append(grades[i])
    return new_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

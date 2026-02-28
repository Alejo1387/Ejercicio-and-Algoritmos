# def minutesBeforeYear(h, m):
#     return ((24 - h) * 60) - m

# print(minutesBeforeYear(23, 55))
# print(minutesBeforeYear(23, 0))
# print(minutesBeforeYear(0, 1))
# print(minutesBeforeYear(4, 20))
# print(minutesBeforeYear(23, 59))

import sys

# For single line input
line = int(sys.stdin.readline())

def minutesBeforeYear(h, m):
    return ((24 - h) * 60) - m

# For single integer
# n = int(sys.stdin.readline())

# For multiple integers
# a, b = map(int, sys.stdin.readline().split())
# minutesBeforeYear(a, b)

# For list of integers
for i in range(line):
    h, m = map(int, sys.stdin.readline().split())
    print(minutesBeforeYear(h, m))
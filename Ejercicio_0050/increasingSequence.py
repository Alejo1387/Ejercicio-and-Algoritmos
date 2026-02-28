import sys

n, d = map(int, sys.stdin.readline().split())
array =  list(map(int, sys.stdin.readline().split()))

# n = 4
# d = 2
# array = [1, 3, 3, 2]
steps = 0

for i in range(1, n):
    while array[i] <= array[i-1]:
        cal = array[i-1] - array[i] + 1
        step = (cal + d - 1) // d
        array[i] += step * d
        steps += step

print(steps)
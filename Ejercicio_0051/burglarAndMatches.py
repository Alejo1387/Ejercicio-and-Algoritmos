import sys

n, d = map(int, sys.stdin.readline().split())

# n, d = 7, 3
# array1 = [[5, 10], [2, 5], [3, 6]]
arr = []

for _ in range(d):
    a, b = map(int, sys.stdin.readline().split())
    arr.append([a, b])

arr.sort(key=lambda x: x[1], reverse=True)

total = 0
numm = n

for a, b in arr:
    if numm == 0:
        break

    take = min(a, numm)
    total += take * b
    numm -= take

print(total)
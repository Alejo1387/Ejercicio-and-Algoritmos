import sys

line = int(sys.stdin.readline())
# line = 4
# array = ['Alex', 'Iván', 'romano', 'Iván']
order = {}

for i in range(line):
    arr = sys.stdin.readline()
    # arr = array[i]
    if arr in order:
        del order[arr]
    order[arr] = True

for name in reversed(order.keys()):
    print(name)
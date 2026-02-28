def minutesBeforeYear(h, m):
    return ((24 - h) * 60) - m

print(minutesBeforeYear(23, 55))
print(minutesBeforeYear(23, 0))
print(minutesBeforeYear(0, 1))
print(minutesBeforeYear(4, 20))
print(minutesBeforeYear(23, 59))
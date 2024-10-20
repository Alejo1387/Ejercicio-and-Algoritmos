def second():
    arr2 = list(arr)
    
    min = arr2[0]
    for k in range(n):
        if arr2[k] < min:
            min = arr2[k]
    max2 = min
    
    max = arr2[0]
    for j in range(n):
        if arr2[j] > max:
            max2 = max
            max = arr2[j]
        elif arr2[j] >= max2 and arr2[j] < max:
            max2 = arr2[j]
            
    print(max2)

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    second()
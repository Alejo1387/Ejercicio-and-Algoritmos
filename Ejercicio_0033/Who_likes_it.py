num = int(input("\nDime la cantidad de me gusta:  "))

array_like = []

for i in range(num):
    name = input("\nDime el " + str(i+1) + " me gusta:  ").title()
    array_like.append(name)

if num < 0:
    print("\nError\n")
elif num == 0:
    print("\nNo one likes this\n")
elif num >= 1 and num <= 3:
    if num == 1:
        print("\n" + array_like[0] + " likes this\n")
    elif num == 2:
        print("\n" + array_like[0] + " and " + array_like[1] + " likes this\n")
    else:
        print("\n" + array_like[0] + ", " + array_like[1] + " and " + array_like[2] + " likes this\n")
else:
    print("\n" + array_like[0] + ", " + array_like[1] + " and " + str(num - 2) + " likes this\n")
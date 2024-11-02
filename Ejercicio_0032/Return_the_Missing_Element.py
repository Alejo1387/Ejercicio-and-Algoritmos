array = []
string = "["

print("\nNumeros unicos del 0 al 9\n")

for i in range(9):
    number = int(input("\nDime el " + str(i+1) + " de la lista:  "))
    while number in array:
        number = int(input("\nDime otro numero en la posicion " + str(i+1) + " de la lista:  "))
    array.append(number)

for k in range(9):
    if k < 8:
        string += str(array[k]) + ", "
    elif k == 8:
        string += str(array[k]) + "]"

for j in range(10):
    if j not in array:
        print("\n\nFalta el " + str(j) + " en el array: " + string + "\n")
        break
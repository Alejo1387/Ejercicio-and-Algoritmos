def numeros():
    can_pos = 0
    neg = 0
    for i in range(cantidad_array):
        if array[i] > 0:
            can_pos+=1
        if array[i] < 0:
            neg+=array[i]
    print(f"""
        Array:
        {array}
        
        Cantidad de positivos: {can_pos}
        
        suma de negativos: {neg}
        """)

cantidad_array = int(input("\nCantidad de numeros:  "))

array = []

for i in range(cantidad_array):
    num = int(input("\nDime el "+str(i+1)+" elemento del array:  "))
    array.append(num)

numeros()
def array_min_max():
    min = array[0]
    max = array[0]
    for i in range(len(array)):
        if array[i] < min:
            min = array[i]
        if array[i] > max:
            max = array[i]
    print(f"""
        Array:
        {array}
        
        Numero minimo:
        {min}
        
        Numero maximo:
        {max}
        """)

cantidad_array = int(input("\nDime la cantidad de numeros en el array:  "))

array = []

for i in range(cantidad_array):
    num_input = int(input("\nDime el "+str(i+1)+" elemento del array:  "))
    array.append(num_input)

array_min_max()
# Enter your code here. Read input from STDIN. Print output to STDOUT

# entrada del tamaño de la matriz y de los conjuntos
a = input()

# entrada de la matriz
matriz = input()
# pasamos a una lista
matriz = matriz.split()

# entrada del 1 conjunto
conj1 = input()
# pasamos a una lista
conj1 = conj1.split()

# entrada del 2 conjunto
conj2 = input()
# pasamos a una lista
conj2 = conj2.split()

# pasamos los conjustos a sets para busquedas rapidas
conj1, conj2 = set(conj1), set(conj2)

# variable para mostrar el resultado
felicidad = 0
       
# hacemos las busquedas 
for num in matriz:
    if num in conj1:
        felicidad += 1
    if num in conj2:
        felicidad -= 1

# mostramos el resultado
print(felicidad)
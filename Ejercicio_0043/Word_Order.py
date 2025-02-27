# Enter your code here. Read input from STDIN. Print output to STDOUT

# pedimos la cantidad de palabras
n = int(input())

# creamos un diccionario
lista_xr = {}

# hacemos un ciclo
for i in range(n):
    # entrada de la palabra
    world = input()
    # verificamos si la palabra esta en el diccionario
    if world not in lista_xr:
        # si esta lo añade y le da un valor de 0
        lista_xr[world] = 0
    # aqui aumentamos su valor
    lista_xr[world] += 1

# aqui cojemos solo los valores y los ponemos en una lista
k = list(lista_xr.values())
    
# mostramos la cantidad de palabras
print(len(lista_xr))
# mostramos las veces que se repite
print(" ".join(map(str, k)))
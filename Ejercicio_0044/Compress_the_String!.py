# Enter your code here. Read input from STDIN. Print output to STDOUT

# importamos esto para hacer la tarea rapida
from itertools import groupby

# cadena de entrada
cadena = input()

# string para guardar los resultados
listas = ""

# ciclo, donde key es el numero donde estamos, group es cuantas veces consecutivas se repite y groupby ponemos la cadena
for key, group in groupby(cadena):
    # aqui pasamos todo a un string
    n = "(" + str(len(list(group))) + ", " + str(int(key)) + ") "
    # aqui lo agregamos
    listas += n

# mostramos el resultado
print(listas)
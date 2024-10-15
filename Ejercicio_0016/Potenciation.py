def potencia(x, y):
    result2, result = x, x
    if x == 0:
        if y == 0:
            result = 1
        else:
            result = 0
    elif y == 0:
        result = 1
    else:
        i = 1
        while i < y:
            result *= result2
            i+=1
    print(f"""
                     {y}
    El resultado de {x}     es igual a {result}
        """)

num1 = int(input("\nDame el numero de la base de la potencia:  "))

while num1 < 0:
    num1 = int(input("\nSolo numero natural para base de la potencia:  "))

num2 = int(input("\nDame el numero de la potencia:  "))

while num2 < 0:
    num2 = int(input("\nSolo numero natural para de la potencia:  "))

potencia(num1, num2)
num1 = int(input("Dime el primer numero: "))
num2 = int(input("\nDime el segundo numero: "))
signo = input("\nDime la operacion: ")
if signo=="+":
    print("\nEl resultado es: ", num1 + num2)
elif signo=="-":
    print("\nEl resultado es: ", num1 - num2)
elif signo=="*":
    print("\nEl resultado es: ", num1 * num2)
elif signo=="/":
    print("\nEl resultado es: ", num1 / num2)
else:
    print("     ERROR     ")
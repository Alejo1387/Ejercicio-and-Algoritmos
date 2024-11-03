def contraparte(n):
    if float(num) == 0:
        print("\nEl 0 no tiene contraparte\n")
    elif float(n) > 0:
        print(f"\n\nNumero: {num}\nContraparte: -{num}\n")
    else:
        print(f"\n\nNumero: {num}\nContraparte: {num[1:]}\n")

num = input("\nEscribe el numero:  ")
contraparte(num)
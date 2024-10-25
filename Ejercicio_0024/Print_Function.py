def mostrar():
    mostrar2 = ""
    for i in range(n):
        mostrar2 += f"{i+1}"
    print(mostrar2)

if __name__ == '__main__':
    n = int(input())
    mostrar()
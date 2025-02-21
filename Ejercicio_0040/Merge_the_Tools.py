def merge_the_tools(string, k):
    # your code goes here
    
    # Hago los arraays
    array = [string[i:i+k] for i in range(0, len(string), k)]
    result = []
    
    # Modifico los repetidos
    for cadenaT in array:
        cadena = ""
        for text in cadenaT:
            if text not in cadena:
                cadena += text
        result.append(cadena)
        
    # Imprimo
    for cadena in result:
        print(cadena)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
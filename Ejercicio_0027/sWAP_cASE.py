def swap_case(s):
    # solucion 1
    # return s.swapcase()
    
    # solucion 2
    array_min = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]
    array_may = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
    ]
    
    new_string = ""
    valor = False
    
    for i in range(len(s)):
        for j in range(len(array_min)):
            if s[i] == array_min[j]:
                new_string += array_may[j]
                valor = True
            elif s[i] == array_may[j]:
                new_string += array_min[j]
                valor = True
        if valor:
            valor = False
        else:
            new_string += s[i]

    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
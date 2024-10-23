def calificacion():
    min = []
    for i in range(len(array)):
        min.append(array[i][1])
    new_min = list(set(min))
    new_min.sort()
    new_list = []
    for j in range(len(array)):
        if array[j][1] == new_min[1]:
            new_list.append(array[j])
    new_list.sort()
    mensaje = ""
    for k in range(len(new_list)):
        if k < (len(new_list) - 1):
            mensaje += new_list[k][0] + "\n"
        else:
            mensaje += new_list[k][0]
    print(mensaje)
if __name__ == '__main__':
    array = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        array.append([name, score])
    calificacion()
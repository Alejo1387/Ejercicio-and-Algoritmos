texto = input("\nIntroduce el String:\n")
texto1 = texto + " "

array = []
textoArray=""

for i in range(len(texto1)):
    if texto1[i] != " ":
        textoArray = textoArray + texto1[i]
    elif texto1[i] == " ":
        array.append(textoArray)
        textoArray=""
        continue

print(f"\ntexto: {texto}\nArray: {array}\n")
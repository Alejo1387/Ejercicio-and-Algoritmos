texto = input("\nEscribe la cadena: ").lower()

polish = {
    "ą" : "a",
    "ć" : "c",
    "ę" : "e",
    "ł" : "l",
    "ń" : "n",
    "ó" : "o",
    "ś" : "s",
    "ź" : "z"
}

new_cadena = ""

for i in range(len(texto)):
    if texto[i] in polish:
        new_cadena = new_cadena + polish[texto[i]]
    else:
        new_cadena = new_cadena + texto[i]

print("\nResultado: " + new_cadena + "\n")
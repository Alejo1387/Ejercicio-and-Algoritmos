import random

number_machina = random.randint(1, 3)

if number_machina == 1:
    opcion_machina = "Tijera"
elif number_machina == 2:
    opcion_machina = "Papel"
elif number_machina == 3:
    opcion_machina = "Piedra"

opcion_person = int(input("""
Vamos a jugar Piedra, Papel y Tijera, estas son las opciones:

    1. Piedra
    2. Papel
    3. Tijera

Elije la opcion numerica: """))

if opcion_person == 1:
    opcion_person = "Piedra"
elif opcion_person == 2:
    opcion_person = "Papel"
elif opcion_person == 3:
    opcion_person = "Tijera"
else:
    print("\n   Error   \n")

if opcion_machina == opcion_person:
    print(f"""
    Maquina:    {opcion_machina}
    Tú:         {opcion_person}
    Resulatdo:  Empate!!
    """)
elif opcion_machina == "Papel":
    if opcion_person == "Tijera":
        print(f"""
    Maquina:    {opcion_machina}
    Tú:         {opcion_person}
    Resulatdo:  Ganaste!!
    """)
    elif opcion_person == "Piedra":
        print(f"""
    Maquina:    {opcion_machina}
    Tú:         {opcion_person}
    Resulatdo:  Perdiste!!
    """)
elif opcion_machina == "Piedra":
    if opcion_person == "Papel":
        print(f"""
    Maquina:    {opcion_machina}
    Tú:         {opcion_person}
    Resulatdo:  Ganaste!!
    """)
    elif opcion_person == "Tijera":
        print(f"""
    Maquina:    {opcion_machina}
    Tú:         {opcion_person}
    Resulatdo:  Perdiste!!
    """)
elif opcion_machina == "Tijera":
    if opcion_person == "Piedra":
        print(f"""
    Maquina:    {opcion_machina}
    Tú:         {opcion_person}
    Resulatdo:  Ganaste!!
    """)
    elif opcion_person == "Papel":
        print(f"""
    Maquina:    {opcion_machina}
    Tú:         {opcion_person}
    Resulatdo:  Perdiste!!
    """)
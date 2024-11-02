import random

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

string = "("

for i in range(10):
    if i < 2:
        number_aleatorio = random.choice(numbers)
        string += str(number_aleatorio)
    elif i == 2:
        number_aleatorio = random.choice(numbers)
        string += str(number_aleatorio) + ") "
    elif i < 5:
        number_aleatorio = random.choice(numbers)
        string += str(number_aleatorio)
    elif i == 5:
        number_aleatorio = random.choice(numbers)
        string += str(number_aleatorio) + "-"
    else:
        number_aleatorio = random.choice(numbers)
        string += str(number_aleatorio)

print("\n" + string + "\n")
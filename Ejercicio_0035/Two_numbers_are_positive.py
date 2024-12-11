import os

numbers = "("
n = 0
os.system("clear")
num = int(input("Dame el 1 numero:  "))
if num > 0:
    n += 1
numbers += str(num) + ", "
os.system("clear")

num = int(input("Dame el 2 numero:  "))
if num > 0:
    n += 1
numbers += str(num) + ", "
os.system("clear")

num = int(input("Dame el 3 numero:  "))
if num > 0:
    n += 1
numbers += str(num) + ")"
os.system("clear")

if n == 2:
    print(f"{numbers}  ->  True\n\n")
else:
    print(f"{numbers}  ->  False\n\n")
X = float(input("\nDame el numero de X:  "))
while X==0:
    X = float(input("\nDame un numero distinto a 0:  "))
    
Y = float(input("\nDame el numero de Y:  "))
while Y==0:
    Y = float(input("\nDame un numero distinto a 0:  "))
    
if X>0 and Y>0:
    print(f"\nLos datos ({X}, {Y}) estan en el cuadrante 1")
elif X<0 and Y>0:
    print(f"\nLos datos ({X}, {Y}) estan en el cuadrante 2")
elif X<0 and Y<0:
    print(f"\nLos datos ({X}, {Y}) estan en el cuadrante 3")
else:
    print(f"\nLos datos ({X}, {Y}) estan en el cuadrante 4")
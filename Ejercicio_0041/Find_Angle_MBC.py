# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

# Valores
AB = int(input())
BC = int(input())

# Hipotenusa
H = math.sqrt(AB**2 + BC**2)

# Calculamos la longitub de M a B
MB = H/2

# Radianes
R1 = math.atan(AB/BC)

# Grados
R2 = math.degrees(R1)

# Redondeo
R3 = round(R2)

# Redondeo
print(str(R3)+chr(176))
# Ejercicio 2
# Dadas dos cadenas, s1 y s2, cree una nueva cadena agregando s2 en medio de s1

import math

str1 = input("Inserta la primera cadena: ")
str2 = input("Inserta la seegunda cadena: ")
strNew = ""

mitadStr1 = math.trunc(len(str1)/2)

for x in str1:
    if x == mitadStr1:
        strNew+= str2
    else:
        strNew+=x

print(strNew)


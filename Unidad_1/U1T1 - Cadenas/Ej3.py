# Ejercicio 3
# Dadas dos cadenas, s1 y s2 devuelven una nueva cadena compuesta por el primer, 
# el medio y el último carácter de cada cadena de entrada

# Import math Library
import math

str1 = input("Introduce la primera cadena: ")
str2 = input("Introduce la segunda cadena: ")

characterM2 = math.trunc(len(str1)/2)
characterM1 = math.trunc(len(str2)/2)

strNew=str1[0]+str2[0]+str1[characterM1]+str2[characterM2]+str1[len(str1)-1]+str2[len(str2)-1]

print(strNew)



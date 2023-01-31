# Ejercicio 18
# Reemplace cada puntuación con # en la siguiente cadena

from string import punctuation

str = input("Introduce una cadena: ")

chr ="#"
for char in punctuation:
    str = str.replace(char,chr)

print(str)


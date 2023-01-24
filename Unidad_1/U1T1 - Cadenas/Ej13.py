
# Ejercicio 13
# Divida una cadena dada con guiones en varias subcadenas y muestre cada subcadena.

str = input('Escribe una cadena con guines: ')

for x in str.split("-"):
    print(x)
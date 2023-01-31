# Ejercicio 16
# Eliminación de todos los caracteres que no sean enteros de una cadena
str = input("Introduce una cadena: ")
strN =""

for x in str:
    if x.isnumeric():
        strN = strN+x

print(strN)

## isdigit()

# Ejercicio 15
# Eliminar símbolos / puntuación especiales de una cadena determinada

str = input("Introduce una cadena: ")
strN =""

for x in str:
    if x.isalnum() or x==" ":
        strN = strN+x

print(strN)
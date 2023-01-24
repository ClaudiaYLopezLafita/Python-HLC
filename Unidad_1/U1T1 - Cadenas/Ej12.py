
# Ejercicio 12
# Encuentre la última posición de una subcadena "Chema" en una cadena determinada

str = input("Introduce una cadena: ")
subStr = input("Introduce la subcadena que quieres buscar: ")

post = str.rfind(subStr)

print(f"La última posición de la subcadena es: {post}")

# Ejercicio 9
# Dada una cadena, devuelve la suma y el promedio de los dígitos que aparecen en la cadena, 
# ignorando todos los demás caracteres.

str = input("Introduce una cadena: ")
sum =0
cont =0

for x in str.split(" "):
    if x.isnumeric():
        x = int(x)
        sum = sum +x
        cont = cont + 1

promedio = sum/cont

print(f"La suma de los digitos es: {sum}")
print(f"El promedio de los digitos: {promedio}")
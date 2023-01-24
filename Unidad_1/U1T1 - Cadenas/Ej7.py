# Ejercicio 7
# Prueba de equilibrio de caracteres de cadena. Asumiremos que una cadena s1 y s2 
# está equilibrada si todos los caracteres de s1 están en s2. la posición de los caracteres no importa.

str1 = input("Introduce la primera cadena: ")
str2 = input("Introduce la segunda cadena: ")

cont = 0

for x in str1:
    for y in str2:
        if x == y:
            cont = cont +1 
        

if cont==len(str1):
    print("True")
else:
    print("False")

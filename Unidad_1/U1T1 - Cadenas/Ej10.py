
# Ejercicio 10
# Dada una cadena de entrada, cuente las apariciones de todos los caracteres dentro de una cadena

str = input("Introduce una cadena: ")

counts = {}
for character in str.replace(" ",""):
    if character in counts:
        counts[character] += 1
    else:
        counts[character] = 1

print(counts)
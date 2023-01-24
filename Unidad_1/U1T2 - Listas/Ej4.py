# Concatenar dos listas en el siguiente orden:
# ['Hola guapo', 'Hola señor', 'toma guapo', 'toma señor']

lista1 = ["Hola ", "toma "]
lista2 = ["guapo", "señor"]

result = []

for x in lista1:
    for y in lista2:
        result.append(x+" "+y)

print(result)
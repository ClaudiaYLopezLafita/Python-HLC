#Eliminar un conjunto de claves de un diccionario

diccionario = {
    "nombre": "Pikolo",
    "edad": 28,
    "salario": 8000,
    "planeta": "Namek"
    }

keysToRemove = ["nombre", "salario"]

for x in range(len(keysToRemove)):
    diccionario.pop(keysToRemove[x])

print(diccionario)
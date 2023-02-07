# Cambiar el nombre de la clave planeta a localizacion en el siguiente diccionario

diccionario = {
    "nombre": "Pikolo",
    "edad": 28,
    "salario": 8000,
    "planeta": "Namek"
}

new_key_assign = { "nombre" : "nombre", "edad" : "edad", "salario" : "salario", "planeta":"localizacion" }

diccionario_new = dict([(new_key_assign.get(key), value) for key, value in diccionario.items()])

print(diccionario_new)
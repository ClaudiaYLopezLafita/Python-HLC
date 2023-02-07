# Obtenga la clave de un valor mínimo del siguiente diccionario

diccionario = {
    'Física': 82,
    'Matemáticas': 65,
    'Historia': 75
}
d_values = list(diccionario.values())
d_values.sort()
min_value = d_values[0]
## primero obtenemos el indice del valor y luego la key con dicho indice
key = list(diccionario.keys())[list(diccionario.values()).index(min_value)]

print(key)



diccionario = {'uno': 1, 'dos': 2, 'tres': 3}
print(diccionario)

print(diccionario['uno'])

# Añadir items
diccionario["cuatro"] = 5
print(diccionario)

# Modificar items (valores)
diccionario["cuatro"] = 4
diccionario.update({'uno': 23})  # otra manera
print(diccionario)

# Eliminar ítems
diccionario.pop("cuatro")
del diccionario["dos"]  # otra manera

# El método .clear() vacía el diccionario (la variable sigue
# siendo un diccionario pero no tiene elementos)
diccionario.popitem()  # Elimina el último elemento insertado

# Se pueden usar Tuplas
tupla = ("hola", "adios", "hasta luego")
dic = {tupla[0]: "saludo1", tupla[1]: "saludo2", tupla[2]: "saludo3"}
print(dic)

id_soft = {"Presidente": "Jon Carmack", "Fundación": 1991,
            "Empleados": 230,
            "videojuegos": ["Doom", "Quake", "Rage"]}
print(id_soft)

id_soft = {"Presidente": "Jon Carmack", "Fundación": 1991, "Empleados": 230,
            "videojuegos": [{"Doom": [1, 2, "Final", 64, 3, 2016, "Eternal"]},
                            "Quake", "Wolfenstein"]}
print(id_soft)


print(id_soft.keys())  # Lista con las claves
print(id_soft.values())  # Lista con los valores
print(id_soft.items())  # Lista de tuplas con claves y valores
print(len(id_soft))

# OJO. Al igual que las listas, copiar no se puede hacer con dict2 = dict1.
# Esto copia la referencia. Hay que llamar al método copy() o utilizar el
# constructor dict().
diccionario_nuevo = id_soft.copy()
diccionario_nuevo_2 = dict(id_soft)

# También podemos construir diccionarios con el operador ** (Kwargs).
# Y podemos unir dos o más diccionarios en su manera de construirlo
# Este operador lo que hace es expandir el diccionario en sus elementos
union_de_diccionarios = {**id_soft, **dic}

# Ojo, que obviamente si añadimos claves que se repiten en los diccionarios,
# se machacará.
pedro = {"edad": 345, "nombre": "pedro", "apellido": "larrubia"}
raul = {"edad": 14, "nombre": "raul"}

fusion = {**pedro, **raul}
# Imprime {'edad': 14, 'nombre': 'raul', 'apellido': 'larrubia'}
print(fusion)
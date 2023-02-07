## TUPLAS
# ¿Qué son las tuplas?

# Listas inmutables, es decir, no se pueden modificar después de su creación.
#  - No permiten añadir, eliminar, mover elementos, etc (no append, extend, remove)
#  - Si permiten extraer porciones, pero el resultado de la extracción es una tupla nueva
#  - Si permiten comprobar si un elemento se encuentra en la tupla

# ¿Qué utilidad o ventaja tienen respecto a las listas?
#  - Más rápidas
#  - Menos espacio (mayor optimización)
#  - Formatean Strings
#  - Pueden utilizarse como claves en un diccionario (las listas no)

# Sintaxis básica
# nombreTupla=(elem1, elem2, elem3, ...)

# Todas las reglas de las listas acerca de los índices se pueden aplicar a las tuplas
mi_tupla = ("Juan", 13, 1, 1995, 13)
print(mi_tupla[1])
print(mi_tupla[:])

# Se pueden construir listas a partir de las tuplas
mi_lista = list(mi_tupla)
print(mi_lista)

# Y viceversa
otra_tupla = tuple(mi_lista)
print(otra_tupla)

# Como en las listas, podemos comprobar si está un elemento de manera booleana
print("Juan" in mi_tupla)

# Podemos saber cuantos veces está el elemento en la tupla
print(mi_tupla.count(13))

# Y saber también la longitud de la tupla
print(len(mi_tupla))

# Tuplas unitarias
# Importante la coma, si no, no es una tupla unitaria (sería solo el elemento, sin "tupla")
tupla_unitaria = ("Juan",)
print(tupla_unitaria)

# Otra sintaxis (empaquetado de tupla)
ultima_tupla = ("Juan", 13, 1, 1995)
nombre, dia, mes, anyo = ultima_tupla  # Desempaquetado
print(nombre)
print(dia)
print(anyo)
print(mes)


### dudas

mi_tupla = ("Juan", 13, ["a", "b"], 1995, 13)
print(mi_tupla)
mi_tupla[2].append("c")
print(mi_tupla)
mi_tupla[0] += "a"
print(mi_tupla)
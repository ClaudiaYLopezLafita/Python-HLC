# Estructura de datos que nos permite almacenar gran cantidad de valores
# (equivalente a los array en otros lenguajes de programación)

# En Python las listas pueden guardar diferente tipo de valores
# (en otros lenguajes no ocurre esto con los array)

# Se pueden expandir dinámicamente añadiendo nuevos elementos
# (otra novedad respecto a los arrays en otros lenguajes)

# Sintaxis básica
# nombreLista=[elem1, elem2, elem3,...]
# Para seleccionar elementos de una lista, requerimos de un índice. Empieza por 0

miLista = ["Chema", "Juan Diego", "Alejandro", "Diana"]

print(miLista[:])  # Imprimimos la lista entera
print(miLista[2])  # Un elemento concreto
print(miLista[-2])  # Un elemento concreto
# print(miLista[7])  # Error. Se va de rango. Salta una excepción
# print(miLista[-7])  # ¡Error también! Se va de rango. Salta una excepción

# # Porción/Parte/Trozo/Cacho (slicing) de lista
print(miLista[:3])  # Imprimimos del 0 (incluido) al 2 (excluye el elemento 3)
print(miLista[0:3])  # Imprimimos del 0 (incluido) al 2 (excluye el elemento 3)
print(miLista[1:2])  # Imprimimos del 1 (incluido) al 1 (excluye el elemento 2)
print(miLista[2:])  # Imprimimos del 2 (incluido) hasta el final
# Hay un tercer parámetro en esta notación, y es los "steps", pasos
print(miLista[0:3:2])  # Imprimimos del 0 (incluido) hasta el 3, de 2 en 2
print(miLista[::-1])  # Imprimimos del revés


# Agregar elementos a una lista
miLista.append("Carmen")  # Añade al final de la lista
print(miLista[:])

# Agregar elementos en una posición concreta de la lista
miLista.insert(2, "Pedro")  # Inserta "Pedro" en la posición 2
print(miLista[:])

# Añadir varios elementos a la vez
miLista.extend(["Manolo", "Santi", "Joserra"])  # "Extiende" la lista con otra
print(miLista[:])

# Obtener el índice de un elemento
print(miLista.index("Alejandro"))

# ¿Qué pasa si hay dos Alejandros?
miLista.append("Alejandro")
print(miLista.index("Alejandro"))

# ¿Y si queremos saber de manera booleana si un elemento se encuentra en la lista?
print("Juan Diego" in miLista)
print("Ramiro" in miLista)

# Las listas pueden almacenar elementos de diferentes tipos
otraLista = ["Chema", 5, True, 43.6]
print(5 in otraLista)
print("Chema" in otraLista)

# Eliminar elementos de la listas
otraLista.remove("Chema")
print(otraLista[:])

otraLista.remove(True)
print(otraLista[:])

# ¿Y si hay elementos repetidos? ¿Los borra todos?
otraLista.append(True)
otraLista.append("enmedio")
otraLista.append(True)
print(otraLista[:])
otraLista.remove(True)  # Elimina el primer elemento que se encuentra. ¡SOLO EL PRIMERO!
print(otraLista[:])

# Eliminar el último elemento
otraLista.pop()
print(otraLista[:])

# Unir listas
terceraLista = miLista + otraLista
print(terceraLista[:])

# "Multiplicador" de listas
cuartaLista = miLista*3
print(cuartaLista[:])

# ¿Sirve entonces sumar 3 veces la lista?
# quintaLista = miLista+3   # NOOOOO. Esto falla, no se puede.

# Listas por comprensión (List Comprehension)
# nueva_lista = [expresion bucle_for condiciones]
# Ejemplo:
# Forma "no pitónica" de hacerlo. Esto lo harías de manera "tradicional". 
# Un poco a lo Java
numbers = [1, 2, 3, 4]
results = []
for n in numbers:
    results.append(n + 1)

print(results)

# Forma "pitónica" de hacerlo
results = [n + 1 for n in numbers]
print(results)

# En estas listas por comprensión, se pueden poner condiciones
# Itero por todos los numbers, y para todos ellos, ejecuto "n + 1"
# PERO, solamente si n < 3. En caso contrario, devuelvo "n".
#leemos desde el final hasta el principio
results = [n + 1 if n < 3 else n for n in numbers] #n+1 es elcado en que se cumpla la condicions
print(results)


# Otras utilidades. El "zip". Unir dos listas en modo cremallera (uno de cada).
# en caso de tener listas de diferente long, se hace una cremañana hasta la de menor long
# Esto crea una tupla. Podemos convertir luego a lista con el constructor de lista
a = [1, 2]
b = ["Uno", "Dos"]
c = zip(a, b)

print(list(c))

# Se para en la lista maś corta. Lógico, no hay más elementos para iterar

# OJO. Para copiar listas no vale con poner lista2 = lista1 (modificar en una modifica la otra).
# Esto copia la REFERENCIA.
# De tal manera que si modificamos lista1, también estaríamos modificando lista2.
# Para copiar DE VERDAD, tenemos que utilizar el método copy().
# Ejemplo:

esta_lista = ["mancuernas", "eliptica", "remo"]
mi_copia = esta_lista.copy() #lista nueva
print(mi_copia)

# Otra manera. Mediante el constructor de lista
mi_copia = list(esta_lista)
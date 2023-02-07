# Ordenar una tupla de tuplas por segundo elemento

tupla = (('a', 23),('b', 37),('c', 11), ('d',29))

lista_tupla = list(tupla)

#sort by second element of tuple
lista_tupla.sort(key = lambda x: x[1])

tupla_ordenada = tuple(lista_tupla)
print(tupla_ordenada)
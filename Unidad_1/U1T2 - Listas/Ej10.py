# Dada una lista, elimine todas las ocurrencias de 20 de la lista

lista = [5, 20, 15, 20, 25, 50, 20]

for x in lista:
    if x == 20:
        lista.remove(x)

print(lista)

# result = [x if x!=20 else lista.remove(x) for x in lista]

# print(result)
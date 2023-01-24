# Dada dos listas, itere ambas simultáneamente de modo que lista1 debería mostrar 
# el elemento en el orden original y lista2 en orden inverso

lista1 = [10, 20, 30, 40]
lista2 = [100, 200, 300, 400]

listaI = lista2[::-1]

for x in lista1:
    print(x, listaI[lista1.index(x)], sep=" ")

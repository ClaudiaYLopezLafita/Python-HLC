#Eliminar cadenas vacías de mi lista

lista = ["Chema", "", "Juan Diego", "Diana", "", "Alejandro"]

for x in lista:
    if x == "":
        lista.remove(x)

result = [lista.remove(x) if x=="" else x for x in lista]

print(lista)
print(result)
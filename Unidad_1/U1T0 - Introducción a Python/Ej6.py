#Acepte una lista de 5 números flotantes como entrada del usuario.

# Creamos una lista vacia
lista = []

#Introducimos los datos en la lista indicando un rango
for i in range(0, 5):
    elemento = float(input("Introduce un numero: "))
    lista.append(elemento) # añadimos el elemento

print("")
print(lista)
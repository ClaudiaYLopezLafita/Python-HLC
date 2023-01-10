#Acepte tres cadenas cualquiera de una llamada input(). 
# Escriba un programa para tomar tres nombres como entrada de un usuario 
# con una única llamada a función input().

##OPCION 1: introducir los nombres en nua lista
nombres = []

for i in range(0, 3):
    nombre = input("Introduce un nombre: ")
    nombres.append(nombre)

print(nombres)

##OPCION 2: ir mostrando los nombre por pantalla

for i in range(0, 3):
    nombre = input("Introduce un nombre: ")
    print(nombre)
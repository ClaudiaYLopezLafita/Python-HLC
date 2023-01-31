#Imprima el siguiente patrón. Escriba un programa para imprimir el siguiente patrón 
# de inicio usando el bucle for

rows = int(input("NUmero de filas de la piramide: "))
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
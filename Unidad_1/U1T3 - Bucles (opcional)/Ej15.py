# Usa un bucle para mostrar elementos de una lista dada presentes en posiciones de índice impares

lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in lista:
    if lista.index(i)%2 != 0:
        print(i)
#Escriba un programa para imprimir el siguiente patrón numérico usando un bucle.

#numero inicialización
num = 1
# primer bubcle para las fiñas
for i in range(0, 5):
    num = 1
    #segundo bucle en relación al primero (filas) 
    #para pintar las columnas
    for j in range(0, i+1):
        # imprimimos el numero
        print(num, end=" ")
        #incrementamos el numero
        num = num + 1
    #imprimimos un salto de linea tras cada fila
    print("\r")

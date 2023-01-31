#Escriba un programa para usar el bucle for para imprimir el siguiente patrón numérico inverso:

#numero inicialización
num = 5
# primer bubcle para las fiñas
for i in range(5, 0,-1):
    num=5
    num = num - 1
    #segundo bucle en relación al primero (filas) 
    #para pintar las columnas
    for j in range(i-1,0,-1):
        # print(f"row{i} col {j} num{num}")
        # imprimimos el numero
        print(num, end=" ")
        #incrementamos el numero
        num = num - 1
    #imprimimos un salto de linea tras cada fila
    print("\r")
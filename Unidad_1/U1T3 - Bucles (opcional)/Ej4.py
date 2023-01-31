#Escribe un programa para imprimir la tabla de multiplicar de un número dado. 
# Por ejemplo, num = 2 la salida debe ser

num = int(input("Introduce un número: "))

print(f"La tabla de multiplicar de {num} es: ")
for i in range(1,11):
    print(f"{i} X {num} = {i*num}")
# Escriba un programa para aceptar un número de un usuario y calcular la suma de 
# todos los números desde 1 hasta un número dado. 
# Por ejemplo, si el usuario ingresó 10, la salida debería ser 55 (1+2+3+4+5+6+7+8+9+10)

num = int(input("Introducce un número: "))

x = 1
total = 0

while x <= num:
    total = total+x
    x = x+1

print(f"La suma de todos sus anteriores son: {total}")
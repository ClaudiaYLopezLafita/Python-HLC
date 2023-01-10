#Calcula la multiplicación y la suma de dos números. 
# Dados dos números enteros, devuelve su producto sólo si el 
# producto es mayor que 1000, de lo contrario, devuelve su suma.

num = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro un numero: "))

if num*num2 > 1000:
    print(f"El prodcuto es: {num*num2}")
else:
    print(f"La suma es: {num+num2}")
#Escriba un programa para contar el número total de dígitos en un número usando un ciclo while. 
# Por ejemplo, el número es 75869, por lo que la salida debería ser 5.  

num = 75869
num_digitos=0

while num > 0:
    num_digitos=num_digitos+1
    num=num//10 #dividimos entre 10

print(f"El numero total de digitos de {num} es: {num_digitos}")

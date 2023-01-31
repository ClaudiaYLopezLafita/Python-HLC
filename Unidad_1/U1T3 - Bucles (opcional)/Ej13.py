#Encuentra el factorial de un número dado. Escribe un programa para usar el ciclo para encontrar 
# el factorial de un número dado.

#El factorial (símbolo !) significa que se multiplican todos los números enteros desde el número 
# elegido hasta 1.

num = int(input("numumero para calcular el factorial: "))

def factorial(n):
    if n==0 or n==1:
            resultado=1
    elif n>1:
            resultado=n*factorial(n-1)
    return resultado

print(f"El factorial de {num}! es {factorial(num)}")
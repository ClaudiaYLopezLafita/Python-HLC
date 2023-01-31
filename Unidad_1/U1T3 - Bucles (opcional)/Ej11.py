#Escriba un programa para mostrar todos los números primos dentro de un rango

#Nota: Un número primo es un número que no se puede formar multiplicando otros números enteros. 
# Un número primo es un número natural mayor que 1 que no es producto de dos números naturales 
# más pequeños.

import math
def primos(min,max):
    """
    This function verifies which numbers are prime
    SCOPE: Range indicated between 2 and argument 'max'
    """
    num_primos = []
    rango = range(min,max)
    
    for number in rango:
        #Variable declarations inside for loop
        maximum_posible_divisor = math.ceil(math.sqrt(number))
        isnt_prime = 0
        i = 2
        while (isnt_prime < 1) and (i <= maximum_posible_divisor):
            if number % i == 0:
                isnt_prime += 1

            i+= 1
        
        if (isnt_prime < 1):
            num_primos.append(number)
            
    return num_primos

for i in primos(25,50):
    print(i)
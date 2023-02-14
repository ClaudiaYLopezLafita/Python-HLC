## Escriba un programa para crear una función recursiva para calcular la suma de números del 0 al 10.

## Una función recursiva es una función que se llama a sí misma una y otra vez.

def suma(num):
    suma = 0
    # Suma cada numero dentro de un rango.
    for i in range(0,num+1):
        suma = suma + i
    # Devuelve la suma
    return suma

print(suma(10))